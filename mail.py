import re
import secrets

SYLLABLES = {
    "indonesian": {
        "first": [
            "bu", "di", "an", "de", "ra", "su", "ti", "wa", "jo", "ri",
            "ag", "ma", "yu", "li", "ni", "he", "pu", "ka", "si", "to"
        ],
        "last": [
            "wi", "ja", "ya", "su", "rya", "di", "pra", "ta", "ma", "kus",
            "hand", "ay", "rah", "man", "fir", "man", "ning", "sih", "put", "ri"
        ],
    },
    "european": {
        "first": [
            "li", "em", "no", "ol", "ja", "av", "lu", "mi", "eth", "is",
            "so", "cl", "fi", "el", "os", "ha", "ma", "ry", "ad", "ch"
        ],
        "last": [
            "sm", "ith", "john", "son", "will", "iams", "brown", "gar", "cia", "mill",
            "er", "davis", "rodr", "iguez", "mart", "inez"
        ],
    },
    "korean": {
        "first": [
            "min", "ji", "seo", "yoon", "hyun", "joon", "soo", "eun", "dong", "hye",
            "jae", "sung", "kyu", "woo", "tae", "jin", "ho", "ye", "ra", "beom"
        ],
        "last": [
            "kim", "lee", "park", "choi", "jung", "kang", "cho", "yoon", "han", "lim",
            "shin", "jang", "jo", "bae", "son", "ahn", "go", "yang", "hwang", "kim"
        ],
    },
    "japanese": {
        "first": [
            "ha", "na", "yu", "ki", "so", "ra", "ri", "ku", "mi", "ao",
            "i", "ren", "kai", "to", "shi", "me", "ru", "da", "ya", "ma"
        ],
        "last": [
            "sa", "to", "su", "zu", "ki", "ta", "ka", "wa", "ta", "be",
            "na", "ka", "wa", "ta", "na", "ka", "mi", "ya", "ma", "ki"
        ],
    },
    "nigerian": {
        "first": [
            "chi", "ami", "tem", "tope", "olu", "wa", "seun", "ade", "bayo", "ifu",
            "nya", "chi", "ne", "du", "fo", "la", "sha", "ba", "ba", "tun",
            "ngo", "zi", "eme", "ka"
        ],
        "last": [
            "ade", "ye", "mi", "oka", "for", "nw", "o", "su", "eze", "ig",
            "we", "bel", "lo", "ogun", "leye", "afo", "labi", "oke", "ke", "ony",
            "ema"
        ],
    },
}


def choice(items):
    return secrets.choice(items)


def rand_int(max_exclusive: int) -> int:
    return secrets.randbelow(max_exclusive)


def chance(probability: float) -> bool:
    return rand_int(10_000) < int(probability * 10_000)


def generate_name(culture: str, is_last_name: bool = False) -> str:
    pool = SYLLABLES.get(culture)
    if not pool:
        return "User"
    parts = pool["last"] if is_last_name else pool["first"]
    if not parts:
        return "User"
    count = 1 if is_last_name else (2 if chance(0.7) else 3)
    name = "".join(choice(parts) for _ in range(count))
    return name[:1].upper() + name[1:].lower()


def clean_name(name: str) -> str:
    return re.sub(r"[^a-zA-Z0-9]", "", name)


def generate_random_email(domain: str | None = None) -> str:
    cultures = list(SYLLABLES.keys())
    culture = choice(cultures)
    first_name = generate_name(culture, False)
    last_name = generate_name(culture, True)
    clean_first = clean_name(first_name)
    clean_last = clean_name(last_name)
    separators = [".", "_", ""]
    sep = choice(separators)
    num = str(rand_int(9999)) if chance(0.6) else ""
    local_part = f"{clean_first}{sep}{clean_last}{num}".lower()
    if domain:
        selected_domain = domain
    else:
        common_domains = ["gmail.com", "yahoo.com"]
        rare_domains = ["outlook.com", "hotmail.com", "protonmail.com"]
        selected_domain = choice(common_domains) if chance(0.85) else choice(rare_domains)
    return f"{local_part}@{selected_domain}"


def generate_twitter_username() -> str:
    syll1 = [
        "ka", "ki", "ko", "ra", "ri", "ro", "sa", "shi", "su", "ta",
        "ti", "to", "na", "ni", "no", "mi", "mo", "ya", "yo", "yu",
        "ha", "hi", "ho", "fa", "fi", "fo", "la", "li", "lu", "ma",
        "me", "mo", "an", "al", "ar", "el", "en", "er", "in", "or",
        "ol", "on"
    ]
    syll2 = [
        "ka", "ki", "ko", "na", "ni", "no", "mi", "mo", "sa", "shi",
        "su", "ta", "ti", "to", "ra", "ri", "ro", "ya", "yo", "yu",
        "ha", "hi", "ho", "fa", "fi", "fo", "la", "li", "lu", "an",
        "ar", "el", "en", "er", "or", "ol", "in"
    ]

    def make_name() -> str:
        length = 2 if chance(0.5) else 3
        name = ""
        for i in range(length):
            src = syll1 if i == 0 else syll2
            name += choice(src)
        return name

    first = make_name()
    last = make_name()
    mods = ["", "_", "."]
    mod = choice(mods)
    num = rand_int(10_000_000)
    return f"@{first}{last}{mod}{num}"


def generate_unique_twitter_usernames(count: int) -> list[str]:
    seen = set()
    out = []
    while len(out) < count:
        username = generate_twitter_username()
        if username not in seen:
            seen.add(username)
            out.append(username)
    return out


def generate_unique_emails(count: int, domain: str | None = None) -> list[str]:
    seen = set()
    out = []
    while len(out) < count:
        email = generate_random_email(domain=domain)
        if email not in seen:
            seen.add(email)
            out.append(email)
    return out


if __name__ == "__main__":
    print("Random emails:")
    for _ in range(10):
        print(generate_random_email())
    print("\nRandom emails:")
    for email in generate_unique_emails(10, domain="gmail.com"): // or domain
        print(email)
    print("\nTwitter usernames:")
    for username in generate_unique_twitter_usernames(10):
        print(username)
