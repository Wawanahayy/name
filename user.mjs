
const SYLLABLES = {
  indonesian: {
    first: ["bu", "di", "an", "de", "ra", "su", "ti", "wa", "jo", "ri", "ag", "ma", "yu", "li", "ni", "he", "pu", "ka", "si", "to"],
    // Nama belakang: sering berakhiran -a, -i, -o, -u, -an, -di, -ta
    last: ["wi", "ja", "ya", "su", "rya", "di", "pra", "ta", "ma", "kus", "hand", "ay", "rah", "man", "fir", "man", "ning", "sih", "put", "ri"]
  },
  european: {
    first: ["li", "em", "no", "ol", "ja", "av", "lu", "mi", "eth", "is", "so", "cl", "fi", "el", "os", "ha", "ma", "ry", "ad", "ch"],
    last: ["sm", "ith", "john", "son", "will", "iams", "brown", "gar", "cia", "mill", "er", "davis", "rodr", "iguez", "mart", "inez"]
  },
  korean: {
    first: ["min", "ji", "seo", "yoon", "hyun", "joon", "soo", "eun", "dong", "hye", "jae", "sung", "kyu", "woo", "tae", "jin", "ho", "ye", "ra", "beom"],
    last: ["kim", "lee", "park", "choi", "jung", "kang", "cho", "yoon", "han", "lim", "shin", "jang", "jo", "bae", "son", "ahn", "go", "yang", "hwang", "kim"]
  },
  japanese: {
    first: ["ha", "na", "yu", "ki", "so", "ra", "ri", "ku", "mi", "ao", "i", "ren", "kai", "to", "shi", "me", "ru", "da", "ya", "ma"],
    last: ["sa", "to", "su", "zu", "ki", "ta", "ka", "wa", "ta", "be", "na", "ka", "wa", "ta", "na", "ka", "mi", "ya", "ma", "ki"]
  },
  nigerian: {
    first: ["chi", "ami", "tem", "tope", "olu", "wa", "seun", "ade", "bayo", "ifu", "nya", "chi", "ne", "du", "fo", "la", "sha", "ba", "ba", "tun", "ngo", "zi", "eme", "ka"],
    last: ["ade", "ye", "mi", "oka", "for", "nw", "o", "su", "eze", "ig", "we", "bel", "lo", "ogun", "leye", "afo", "labi", "oke", "ke", "ony", "ema"]
  }
};

function generateName(culture, isLastName = false) {
  const pool = SYLLABLES[culture];
  if (!pool) return "user";

  const parts = isLastName ? pool.last : pool.first;
  if (parts.length === 0) return "user";

  const count = isLastName ? 1 : (Math.random() < 0.7 ? 2 : 3); // depan: 2-3 suku kata, belakang: 1-2
  let name = "";

  for (let i = 0; i < count; i++) {
    const syll = parts[Math.floor(Math.random() * parts.length)];
    name += syll;
  }

  return name.charAt(0).toUpperCase() + name.slice(1).toLowerCase();
}

export function generateRandomEmail() {
  const cultures = Object.keys(SYLLABLES);
  const culture = cultures[Math.floor(Math.random() * cultures.length)];

  const firstName = generateName(culture, false);
  const lastName = generateName(culture, true);

  const cleanName = (name) => name.replace(/[^a-zA-Z0-9]/g, '');

  const cleanFirst = cleanName(firstName);
  const cleanLast = cleanName(lastName);

  const separators = ['.', '_', ''];
  const sep = separators[Math.floor(Math.random() * separators.length)];
  const num = Math.random() > 0.4 ? Math.floor(Math.random() * 9999) : '';
  const localPart = (cleanFirst + sep + cleanLast + num).toLowerCase();

  const commonDomains = ['gmail.com', 'yahoo.com'];
  const rareDomains = ['outlook.com', 'hotmail.com', 'protonmail.com'];
  const domain = Math.random() < 0.85
    ? commonDomains[Math.floor(Math.random() * commonDomains.length)]
    : rareDomains[Math.floor(Math.random() * rareDomains.length)];

  return `${localPart}@${domain}`;
}

function generateTwitterUsername() {
  const syll1 = ["ka","ki","ko","ra","ri","ro","sa","shi","su","ta","ti","to","na","ni","no","mi","mo","ya","yo","yu","ha","hi","ho","fa","fi","fo","la","li","lu","ma","me","mo","an","al","ar","el","en","er","in","or","ol","on"];
  const syll2 = ["ka","ki","ko","na","ni","no","mi","mo","sa","shi","su","ta","ti","to","ra","ri","ro","ya","yo","yu","ha","hi","ho","fa","fi","fo","la","li","lu","an","ar","el","en","er","or","ol","in"];

  function makeName() {
    const length = Math.random() < 0.5 ? 2 : 3;
    let name = "";
    for (let i = 0; i < length; i++) {
      const src = i === 0 ? syll1 : syll2;
      name += src[Math.floor(Math.random() * src.length)];
    }
    return name;
  }

  const first = makeName();
  const last = makeName();
  const mods = ["", "_", "."];
  const mod = mods[Math.floor(Math.random() * mods.length)];
  const num = Math.floor(Math.random() * 10000000);

  return "@" + first + last + mod + num;
}

export function generateUniqueTwitterUsernames(count) {
  const set = new Set();
  const out = [];
  while (out.length < count) {
    const n = generateTwitterUsername();
    if (!set.has(n)) {
      set.add(n);
      out.push(n);
    }
  }
  return out;
}

export { generateRandomEmail, generateTwitterUsername, generateUniqueTwitterUsernames };
export default { generateRandomEmail, generateTwitterUsername, generateUniqueTwitterUsernames };
