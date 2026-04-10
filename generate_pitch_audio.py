"""
Apsara Pitch Deck — 5-Slide Narration Generator
Azure TTS · en-IN-NeerjaNeural
"""
import os
import azure.cognitiveservices.speech as speechsdk

SPEECH_KEY = os.environ.get("AZURE_SPEECH_KEY", "")
SPEECH_REGION = os.environ.get("AZURE_REGION", "centralindia")
VOICE_NAME = "en-IN-NeerjaNeural"
OUTPUT_DIR = os.path.join(os.path.dirname(__file__), "audio", "pitch")

NARRATIONS = {
    1: """
    Invest 15 lakhs today.

    Receive 15,000 rupees every single month, directly into your bank account.

    And at the end of 30 months, walk away with 23 lakh 25 thousand rupees.

    That's a 55 percent return. On land you can see, touch, and own.

    This is the Apsara Growth Partner Programme.
    """,

    2: """
    Here's how it works. Four simple steps.

    Step one: you invest 15 lakhs. A 1,500 square foot plot in Greater Bhubaneswar
    is identified and linked to your name from Day 1.

    Step two: every month, you receive 15,000 rupees via NEFT or RTGS.
    That's 12 percent annual income, contractually committed.

    Step three: this continues for 30 months. You accumulate 4 lakh 50 thousand
    in total income.

    Step four: at Month 30, you choose your exit.
    Either keep the land — with a conservative value of 30 lakhs or more.
    Or take the buyback — 18 lakh 75 thousand, plus the income you've already received.

    Everything is documented in a stamped, court-enforceable MOU before you invest a single rupee.
    """,

    3: """
    Let's talk numbers.

    You put in 15 lakhs. Over 30 months, you receive 4 lakh 50 thousand in monthly income.

    If you choose the buyback exit, the company buys your plot back at 18 lakh 75 thousand.

    Your total cash: 23 lakh 25 thousand. That's 55 percent on your 15 lakhs.

    But here's where it gets interesting.

    If you retain the land instead, comparable corridors in Odisha have appreciated
    2.5 to 4 times after development approvals.

    That puts your 15 lakh plot at 30 to 60 lakhs. And you still keep the 4 lakh 50 thousand
    income you've already received.

    Buyback gives you certainty. Retention gives you wealth.
    The choice is yours, and both are written into your MOU.
    """,

    4: """
    Why this location? And why now?

    The project sits in Bajpur, Khordha — inside the formally notified
    Greater Bhubaneswar Master Plan expansion zone.

    Three forces are converging here. The Odisha Smart City Initiative.
    The Industrial Corridor Expansion. And the state capital's outward growth.

    You're entering at 1,000 rupees per square foot — before RERA registration,
    before price discovery, before the market catches up.

    And your investment is protected. Stamped MOU under the Indian Contract Act.
    MCA-registered company. Payments via banking channels only.
    Five Indian statutes govern this structure.

    You can verify everything — the company on MCA dot gov dot in,
    the land on Bhulekh Odisha. We encourage it.
    """,

    5: """
    15 lakhs. 30 months. 55 percent secured return.

    Or hold the land and let Odisha's growth do the rest.

    Limited plots available at Phase 1 pricing.

    Call or WhatsApp: 93485 31992.

    Email: info at apsararealcon dot in.

    Visit: www dot apsararealcon dot in.

    Become a Growth Partner today.
    """
}


def generate_audio(slide_num, text):
    speech_config = speechsdk.SpeechConfig(subscription=SPEECH_KEY, region=SPEECH_REGION)
    speech_config.speech_synthesis_voice_name = VOICE_NAME
    speech_config.set_speech_synthesis_output_format(
        speechsdk.SpeechSynthesisOutputFormat.Audio16Khz32KBitRateMonoMp3
    )
    output_path = os.path.join(OUTPUT_DIR, f"p{slide_num}.mp3")
    audio_config = speechsdk.audio.AudioOutputConfig(filename=output_path)
    synthesizer = speechsdk.SpeechSynthesizer(speech_config=speech_config, audio_config=audio_config)

    ssml = f"""
    <speak version='1.0' xmlns='http://www.w3.org/2001/10/synthesis' xml:lang='en-IN'>
        <voice name='{VOICE_NAME}'>
            <prosody rate='-8%' pitch='+2%'>
                {text.strip()}
            </prosody>
        </voice>
    </speak>
    """
    print(f"  Slide {slide_num}...", end=" ", flush=True)
    result = synthesizer.speak_ssml_async(ssml).get()
    if result.reason == speechsdk.ResultReason.SynthesizingAudioCompleted:
        size_kb = os.path.getsize(output_path) / 1024
        print(f"OK ({size_kb:.0f} KB)")
        return True
    else:
        print(f"FAILED: {result.cancellation_details.error_details}")
        return False


def main():
    os.makedirs(OUTPUT_DIR, exist_ok=True)
    print(f"Generating pitch narration: {VOICE_NAME}\n")
    ok = sum(generate_audio(i, NARRATIONS[i]) for i in sorted(NARRATIONS))
    print(f"\nDone: {ok}/{len(NARRATIONS)}")


if __name__ == "__main__":
    main()
