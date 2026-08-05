#!/usr/bin/env python3
"""
LinkedIn Post Generator™ Enterprise Edition
=============================================
Sıradan cümleleri, Fortune 500 şirketlerinin C-level yöneticilerinin
gurur duyacağı seviyede abartılı LinkedIn paylaşımlarına dönüştüren
"AI-powered" (aslında if-else) bir Humility Amplification Engine.
"""

import random
import argparse
import textwrap

EMOJIS = ["🚀", "🔥", "💡", "🙌", "📈", "✨", "🎯", "🌱", "🏆", "💪"]

OPENERS = [
    "Büyük bir milestone'u paylaşmaktan gurur duyuyorum!",
    "Bugün sizlerle heyecan verici bir gelişmeyi paylaşmak istiyorum.",
    "Bu bir teşekkür postu... ve biraz da bir başarı hikayesi.",
    "Kariyerimde unutamayacağım bir gün daha.",
    "Bazen küçük adımlar, büyük dönüşümlerin başlangıcı olur.",
    "Bugün ekip olarak birlikte yazdığımız hikayeye yeni bir sayfa ekledik.",
]

BUZZWORD_BRIDGES = [
    "Bu basit görünen adım aslında **customer-centric mindset**, **agile execution** ve **radical ownership** kültürümüzün bir yansıması.",
    "Bu deneyim bana bir kez daha gösterdi ki: **growth mindset** ve **cross-functional collaboration** olmadan hiçbir başarı mümkün değil.",
    "Bunu başarabilmemizin sırrı? **Data-driven decision making**, **psychological safety** ve elbette biraz da **grit**.",
    "İşin özeti: **synergy**, **stakeholder alignment** ve gece yarısı içilen kahveler ☕.",
    "Bu süreç bana **resilience**, **servant leadership** ve **continuous improvement**'ın gerçek anlamını öğretti.",
]

THANKS = [
    "Bu yolculukta bana destek olan herkese, özellikle mentorlarıma ve harika ekibime sonsuz teşekkürler 🙏",
    "Bu başarı bir takım oyunu — desteklerini hiç esirgemeyen tüm ekip arkadaşlarıma teşekkür ederim 🙏",
    "Beni bu noktaya getiren herkese, ailemden yöneticime kadar minnettarım 🙏",
    "Bu paylaşımı, bu süreçte yanımda olan herkese ithaf ediyorum 🙏",
]

CTAS = [
    "Sizin de benzer bir deneyiminiz oldu mu? Yorumlarda paylaşın! 👇",
    "Bu konuda ne düşünüyorsunuz? Fikirlerinizi merak ediyorum. 👇",
    "Benzer bir yolculuktaysanız, bağlantı kurmaktan mutluluk duyarım. 🤝",
    "#Networking her zaman kapımız açık — DM'den ulaşabilirsiniz!",
]

HASHTAG_POOL = [
    "#Leadership", "#Growth", "#TechForGood", "#Innovation", "#Agile",
    "#DigitalTransformation", "#Teamwork", "#Grateful", "#Mindset",
    "#FutureOfWork", "#Synergy", "#PersonalBranding", "#CareerJourney",
    "#AI", "#Blockchain", "#Web3", "#Hustle", "#NeverStopLearning",
]


def amplify(input_sentence: str, humility_level: int = 11) -> str:
    """
    Sıradan bir cümleyi LinkedIn formatına çevirir.

    humility_level: 1-11 arası (11 en abartılı seviyedir, varsayılan budur
    çünkü LinkedIn'de mütevazılık ölçeği zaten hiçbir zaman 10'u geçmez).
    """
    emoji = random.choice(EMOJIS)
    opener = random.choice(OPENERS)
    bridge = random.choice(BUZZWORD_BRIDGES)
    thanks = random.choice(THANKS)
    cta = random.choice(CTAS)
    hashtags = " ".join(random.sample(HASHTAG_POOL, k=min(5, len(HASHTAG_POOL))))

    post = f"""{emoji} {opener}

{input_sentence.strip().capitalize()}.

{bridge}

{thanks}

{cta}

{hashtags}
"""
    return post


def main():
    parser = argparse.ArgumentParser(
        description="Enterprise-grade Humility Amplification Engine"
    )
    parser.add_argument(
        "sentence",
        nargs="?",
        default="Bugün bug fix yaptım",
        help="Dönüştürülecek sıradan cümle (varsayılan: 'Bugün bug fix yaptım')",
    )
    parser.add_argument(
        "-n", "--count", type=int, default=1, help="Kaç varyasyon üretilsin"
    )
    args = parser.parse_args()

    for i in range(args.count):
        print(f"\n{'=' * 50}\nVaryasyon {i + 1}\n{'=' * 50}")
        print(amplify(args.sentence))


if __name__ == "__main__":
    main()
