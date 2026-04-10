"""
Apsara Growth Partner Programme — Voice Narration Generator
Azure Text-to-Speech with Indian Female Voice (Neerja Neural)
"""

import os
import azure.cognitiveservices.speech as speechsdk

SPEECH_KEY = os.environ.get("AZURE_SPEECH_KEY", "")
SPEECH_REGION = os.environ.get("AZURE_REGION", "centralindia")
VOICE_NAME = "en-IN-NeerjaNeural"
OUTPUT_DIR = os.path.join(os.path.dirname(__file__), "audio")

NARRATIONS = {
    1: """
    Welcome to Apsara Realcon's Land-Backed Monthly Income Programme.

    The Greater Bhubaneswar Growth Partner Programme offers a structured,
    land-backed investment with 12 percent annual contractual income.

    Here are the numbers that matter: a minimum entry of 15 lakhs,
    12 percent annual income paid monthly, a total exit value of
    23 lakh 25 thousand rupees, and a clearly defined 30-month programme term.

    All backed by a court-enforceable MOU, with pre-RERA entry pricing.

    Let's walk you through the complete structure.
    """,

    2: """
    This is the programme overview.

    With an investment of 15 lakhs, you receive an identified 1,500 square foot
    plot in the Greater Bhubaneswar corridor.

    The structure is simple. You receive 15,000 rupees every month via
    NEFT or RTGS bank transfer, for 30 months.

    At month 30, you choose: either a registered Sale Deed for your
    identified plot, or a pre-agreed buyback at 18 lakh 75 thousand —
    a 25 percent premium.

    On the right, you can see the complete programme snapshot —
    the project is located in Bajpur, Khordha, Odisha,
    at an entry price of just 1,000 rupees per square foot.

    Please note: this is a pre-RERA structure. The MOU governs your terms.
    Sale Deed follows OdishaRERA registration. Independent due diligence
    is always advised.
    """,

    3: """
    Let's look at the cumulative cash outcome over 30 months.

    You invest 15 lakhs. You receive 15,000 rupees every month.

    In Year 1, you earn 1 lakh 80 thousand in income.
    By Year 2, your cumulative income reaches 3 lakh 60 thousand.
    And at the Month 30 exit, if you choose the buyback option,
    your total cash return is 23 lakh 25 thousand rupees.

    That's a 55 percent total return on your 15 lakh investment —
    comprising 4 lakh 50 thousand in monthly income already received,
    plus the 18 lakh 75 thousand buyback value.

    The bar chart on the left illustrates this progression visually.
    """,

    4: """
    Your MOU defines two clear exit paths. Let's understand both.

    Option A is the long-term wealth path. You receive a Registered
    Sale Deed for your 1,500 square foot plot, plus the 4 lakh 50 thousand
    in income you've already received. Conservative corridor appreciation
    suggests a value of 30 lakhs or more at maturity, especially with
    the Odisha Master Plan expansion.

    Option B is the Capital Buyback. The company buys back your plot
    at 1,250 rupees per square foot — a 25 percent premium over your
    entry price. Combined with the 4 lakh 50 thousand income already
    received, your total cash at exit is 23 lakh 25 thousand rupees.
    That's 55 percent total return on 15 lakhs, over 30 months.

    Both paths are contractually documented in your stamped MOU
    before you invest.
    """,

    5: """
    Why might retaining the land be the smarter choice?

    The conservative minimum appreciation is 2 times your entry price.
    Comparable corridors in Tier-2 Indian cities have delivered
    2.5 to 4 times appreciation post-development approvals.
    That puts the conservative value of your plot at 30 lakhs or more.

    Three macro forces are converging on this corridor simultaneously.

    First, the Odisha Smart City Initiative is driving state-capital expansion.
    Second, the Industrial Corridor Expansion makes this one of India's
    most active infrastructure zones.
    And third, the Greater Bhubaneswar Master Plan formally notifies
    this as an expansion zone.

    Remember — your buyback option stays fully open. You've already
    received 4 lakh 50 thousand in income. You're positioned at the
    front of the price discovery curve.
    """,

    6: """
    Let's explore the strategic location.

    The project is situated in Mouza Bajapur, Tahsil Khorda,
    District Khorda, Odisha — within the Greater Bhubaneswar
    Mega Plotting Corridor.

    Look at the proximity advantages: just 2 kilometres from the
    National Highway, 4.5 kilometres from the Khordha Collectorate,
    2 kilometres from the educational hub, and just 1 kilometre from
    Bajpur Main Market. Hospital and banking facilities are within
    500 metres, and the railway station is 5 kilometres away.

    Bajpur sits within the formally notified Greater Bhubaneswar
    Master Plan expansion zone. Khordha district has the highest
    urbanisation rate in Odisha. And your Phase-1 entry at 1,000
    rupees per square foot positions you before formal price discovery.
    """,

    7: """
    Here's the planned township infrastructure.

    The development features 40-foot main roads and 30-foot internal
    roads — this is what transforms a plotted layout into a liveable
    neighbourhood.

    The planned amenities include a swimming pool, shopping complex,
    modern gymnasium, premium clubhouse, badminton court, indoor games,
    24/7 security, children's park, underground drainage, community hall,
    landscaping, and well-planned road networks.

    Please note — amenity execution is subject to project phasing,
    layout approvals, and the final development rollout.
    """,

    8: """
    This is your milestone journey — a clear, structured roadmap
    from entry to exit.

    Stage 1 is happening now, in 2026. MOU Execution. Your entry
    begins through a stamped MOU with identified project allocation
    and clear commercial terms from Day 1.

    Stage 2 is the Execution Phase — layout planning, title diligence,
    and project preparation.

    Stage 3 is the Approval Stage — project approvals and statutory
    compliance are pursued as part of the formal development roadmap.

    Stage 4 moves to RERA Registration — the final transfer pathway
    through OdishaRERA.

    And Stage 5, at Month 30, is your decision point — retain the land
    for appreciation, or exercise the pre-agreed buyback exit.

    This is a milestone-based journey with visible progress and a
    defined exit framework — not an open-ended proposition.
    """,

    9: """
    This programme is designed for investor confidence,
    with multiple layers of protection.

    Your stamped MOU is executed from the outset — legally binding
    under the Indian Contract Act, 1872. All income payments are made
    via traceable NEFT or RTGS bank transfers. And independent
    verification is actively encouraged.

    Four safeguards define the structure.

    First, Regulatory Process Clarity — the pre-RERA stage is disclosed,
    not hidden.
    Second, Execution Discipline — monthly bank payouts create a
    visible performance trail.
    Third, Defined Exit Protection — both exit paths are documented
    in your MOU before entry.
    And fourth, the MOU-backed structure gives you dual exit flexibility —
    income plus asset, or income plus buyback.
    """,

    10: """
    Your investment is governed by five established Indian statutes.

    RERA 2016 ensures a compliant final transfer.
    The Indian Contract Act of 1872 makes your MOU court-enforceable
    from Day 1.
    The Companies Act 2013 means the operating company —
    Apsara Realcon Private Limited — is MCA-registered and verifiable.
    The Registration Act of 1908 provides a registered document trail.
    And the Income Tax Act of 1961 ensures a fully auditable banking trail.

    You can verify everything yourself. Check the company on
    mca.gov.in. Verify land records on bhulekh.odisha.gov.in.
    Have your lawyer review the MOU. And always pay only via
    NEFT or RTGS.
    """,

    11: """
    Why choose the Apsara Growth Partner Programme? Six clear reasons.

    12 percent annual contractual income — 15,000 rupees per month
    for 30 months, via bank transfer. Not projected — contractually committed.

    A tangible land asset — 1,500 square feet in a master-planned
    corridor with 2 to 4 times appreciation potential.

    MOU protection from Day 1 — court-enforceable under the
    Indian Contract Act.

    Two flexible exits — the buyback gives you 55 percent return,
    or retain for multifold appreciation.

    Entry before full price discovery — Phase-1 at 1,000 rupees
    per square foot, before post-development repricing.

    And an MCA-registered operating company — verifiable on mca.gov.in.

    Your land. Your income. 8 lakh 25 thousand secured profit in
    30 months — or potentially multifold wealth if you hold.
    """,

    12: """
    How does this programme compare to alternatives?

    Against a Bank Fixed Deposit offering 6.5 to 7.5 percent,
    Apsara delivers 12 percent contractual returns plus land
    appreciation upside.

    Against Debt Mutual Funds at 7 to 9 percent with market risk,
    Apsara provides fixed monthly income of 15,000 rupees backed
    by a physical land asset.

    Against raw land which gives zero income and carries liquidity risk,
    Apsara combines monthly income with a defined buyback exit.

    The 30-month total on 15 lakhs: Apsara delivers 23 lakh 25 thousand —
    a 55 percent return. A Bank FD would give approximately 17.8 lakhs.
    A Debt Mutual Fund would be variable between 17 to 19 lakhs.
    And raw land? Unknown and illiquid.

    Income visibility, a secured buyback exit, and land appreciation
    potential — all combined in one structure.
    """,

    13: """
    Are you ready to become a Growth Partner?

    Secure your plot in Greater Bhubaneswar at Phase 1 pricing
    of just 1,000 rupees per square foot. Limited plots available.

    Visit our registered office at Plot Number 132, First Floor,
    Forest Park, Bapujee Nagar, Bhubaneswar, Odisha.

    Call or WhatsApp us at 93485 31992.
    Email us at info at apsararealcon dot in — we respond within
    24 hours.

    Or visit our website at www.apsararealcon.in.

    Thank you for watching. We look forward to welcoming you
    as a Growth Partner.
    """
}


def generate_audio(slide_num, text):
    """Generate audio for a single slide using Azure TTS."""
    speech_config = speechsdk.SpeechConfig(
        subscription=SPEECH_KEY,
        region=SPEECH_REGION
    )
    speech_config.speech_synthesis_voice_name = VOICE_NAME
    speech_config.set_speech_synthesis_output_format(
        speechsdk.SpeechSynthesisOutputFormat.Audio16Khz32KBitRateMonoMp3
    )

    output_path = os.path.join(OUTPUT_DIR, f"slide_{slide_num:02d}.mp3")
    audio_config = speechsdk.audio.AudioOutputConfig(filename=output_path)

    synthesizer = speechsdk.SpeechSynthesizer(
        speech_config=speech_config,
        audio_config=audio_config
    )

    # Use SSML for better control over speech
    ssml = f"""
    <speak version='1.0' xmlns='http://www.w3.org/2001/10/synthesis' xml:lang='en-IN'>
        <voice name='{VOICE_NAME}'>
            <prosody rate='-5%' pitch='+2%'>
                {text.strip()}
            </prosody>
        </voice>
    </speak>
    """

    print(f"  Generating slide {slide_num}...", end=" ", flush=True)
    result = synthesizer.speak_ssml_async(ssml).get()

    if result.reason == speechsdk.ResultReason.SynthesizingAudioCompleted:
        size_kb = os.path.getsize(output_path) / 1024
        print(f"OK ({size_kb:.0f} KB)")
        return True
    else:
        cancellation = result.cancellation_details
        print(f"FAILED: {cancellation.reason} — {cancellation.error_details}")
        return False


def main():
    os.makedirs(OUTPUT_DIR, exist_ok=True)
    print(f"Generating narration with voice: {VOICE_NAME}")
    print(f"Output directory: {OUTPUT_DIR}\n")

    success = 0
    for slide_num in sorted(NARRATIONS.keys()):
        if generate_audio(slide_num, NARRATIONS[slide_num]):
            success += 1

    print(f"\nDone: {success}/{len(NARRATIONS)} audio files generated.")


if __name__ == "__main__":
    main()
