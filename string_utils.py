import re
import json
import hashlib
from typing import List, Dict, Optional, Set
from collections import Counter


def reverse_string(s: str) -> str:
    return s[::-1]


def is_palindrome(s: str) -> bool:
    cleaned = re.sub(r'[^a-zA-Z0-9]', '', s).lower()
    return cleaned == cleaned[::-1]


def count_vowels(s: str) -> int:
    vowels = set('aeiouAEIOU')
    return sum(1 for c in s if c in vowels)


def count_consonants(s: str) -> int:
    return sum(1 for c in s if c.isalpha() and c not in 'aeiouAEIOU')


def capitalize_words(s: str) -> str:
    return ' '.join(word.capitalize() for word in s.split())


def to_snake_case(s: str) -> str:
    s = re.sub(r'([A-Z])', r'_\1', s)
    s = re.sub(r'[\s\-]+', '_', s)
    s = re.sub(r'_+', '_', s)
    return s.strip('_').lower()


def to_camel_case(s: str) -> str:
    words = re.split(r'[\s_\-]+', s)
    return words[0].lower() + ''.join(w.capitalize() for w in words[1:])


def to_pascal_case(s: str) -> str:
    words = re.split(r'[\s_\-]+', s)
    return ''.join(w.capitalize() for w in words)


def truncate(s: str, max_length: int, suffix: str = '...') -> str:
    if len(s) <= max_length:
        return s
    return s[:max_length].rstrip() + suffix


def word_count(s: str) -> int:
    return len(s.split())


def char_frequency(s: str) -> Dict[str, int]:
    return dict(Counter(s))


def most_common_words(s: str, n: int = 5) -> List[tuple]:
    words = re.findall(r'\b\w+\b', s.lower())
    return Counter(words).most_common(n)


def is_anagram(s1: str, s2: str) -> bool:
    return sorted(s1.replace(' ', '').lower()) == sorted(s2.replace(' ', '').lower())


def remove_duplicates(s: str) -> str:
    seen: Set[str] = set()
    result = []
    for c in s:
        if c not in seen:
            seen.add(c)
            result.append(c)
    return ''.join(result)


def find_all_substrings(s: str, sub: str) -> List[int]:
    indices = []
    start = 0
    while True:
        idx = s.find(sub, start)
        if idx == -1:
            break
        indices.append(idx)
        start = idx + 1
    return indices


def longest_common_prefix(strings: List[str]) -> str:
    if not strings:
        return ''
    prefix = strings[0]
    for s in strings[1:]:
        while not s.startswith(prefix):
            prefix = prefix[:-1]
            if not prefix:
                return ''
    return prefix


def levenshtein_distance(s1: str, s2: str) -> int:
    if len(s1) < len(s2):
        return levenshtein_distance(s2, s1)
    if len(s2) == 0:
        return len(s1)
    prev_row = list(range(len(s2) + 1))
    for i, c1 in enumerate(s1):
        curr_row = [i + 1]
        for j, c2 in enumerate(s2):
            insertions = prev_row[j + 1] + 1
            deletions = curr_row[j] + 1
            substitutions = prev_row[j] + (c1 != c2)
            curr_row.append(min(insertions, deletions, substitutions))
        prev_row = curr_row
    return prev_row[-1]


def contains_only_digits(s: str) -> bool:
    return s.isdigit()


def contains_only_letters(s: str) -> bool:
    return s.isalpha()


def contains_only_alphanumeric(s: str) -> bool:
    return s.isalnum()


def extract_emails(s: str) -> List[str]:
    pattern = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'
    return re.findall(pattern, s)


def extract_urls(s: str) -> List[str]:
    pattern = r'https?://(?:[-\w.]|(?:%[\da-fA-F]{2}))+(?::\d+)?(?:/[\w\-./?%&=]*)?'
    return re.findall(pattern, s)


def extract_phone_numbers(s: str) -> List[str]:
    pattern = r'\b\d{3}[-.]?\d{3}[-.]?\d{4}\b'
    return re.findall(pattern, s)


def mask_email(email: str) -> str:
    parts = email.split('@')
    if len(parts) != 2:
        return email
    name = parts[0]
    if len(name) <= 2:
        masked = name[0] + '***'
    else:
        masked = name[0] + '***' + name[-1]
    return masked + '@' + parts[1]


def mask_credit_card(number: str) -> str:
    clean = number.replace(' ', '').replace('-', '')
    if not clean.isdigit() or len(clean) < 13:
        return number
    return '****-****-****-' + clean[-4:]


def generate_slug(s: str) -> str:
    s = s.lower().strip()
    s = re.sub(r'[^\w\s-]', '', s)
    s = re.sub(r'[\s_]+', '-', s)
    s = re.sub(r'-+', '-', s)
    return s.strip('-')


def rot13(s: str) -> str:
    result = []
    for c in s:
        if 'a' <= c <= 'z':
            result.append(chr((ord(c) - ord('a') + 13) % 26 + ord('a')))
        elif 'A' <= c <= 'Z':
            result.append(chr((ord(c) - ord('A') + 13) % 26 + ord('A')))
        else:
            result.append(c)
    return ''.join(result)


def sha256_hash(s: str) -> str:
    return hashlib.sha256(s.encode()).hexdigest()


def md5_hash(s: str) -> str:
    return hashlib.md5(s.encode()).hexdigest()


def base64_encode(s: str) -> str:
    import base64
    return base64.b64encode(s.encode()).decode()


def base64_decode(s: str) -> str:
    import base64
    return base64.b64decode(s.encode()).decode()


def is_valid_email(s: str) -> bool:
    pattern = r'^[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}$'
    return bool(re.match(pattern, s))


def is_strong_password(s: str) -> bool:
    if len(s) < 8:
        return False
    if not re.search(r'[A-Z]', s):
        return False
    if not re.search(r'[a-z]', s):
        return False
    if not re.search(r'[0-9]', s):
        return False
    if not re.search(r'[!@#$%^&*(),.?":{}|<>]', s):
        return False
    return True


def wrap_text(s: str, width: int) -> List[str]:
    words = s.split()
    lines = []
    current = []
    current_len = 0
    for word in words:
        if current_len + len(word) + len(current) > width:
            lines.append(' '.join(current))
            current = [word]
            current_len = len(word)
        else:
            current.append(word)
            current_len += len(word)
    if current:
        lines.append(' '.join(current))
    return lines


def indent_text(s: str, level: int = 1, indent_char: str = '  ') -> str:
    indent = indent_char * level
    return indent + ('\n' + indent).join(s.splitlines())


def strip_html_tags(s: str) -> str:
    return re.sub(r'<[^>]+>', '', s)


def to_boolean(s: str) -> Optional[bool]:
    s = s.strip().lower()
    if s in ('true', '1', 'yes', 'y', 'on'):
        return True
    if s in ('false', '0', 'no', 'n', 'off'):
        return False
    return None


def pluralize(word: str, count: int = 2) -> str:
    if count == 1:
        return word
    if word.endswith(('s', 'x', 'z', 'ch', 'sh')):
        return word + 'es'
    if word.endswith('y') and len(word) > 2 and word[-2] not in 'aeiou':
        return word[:-1] + 'ies'
    return word + 's'


def ellipsize(s: str, max_len: int) -> str:
    if len(s) <= max_len:
        return s
    return s[:max_len - 3] + '...'


def camel_to_snake(s: str) -> str:
    s = re.sub(r'([A-Z]+)([A-Z][a-z])', r'\1_\2', s)
    s = re.sub(r'([a-z0-9])([A-Z])', r'\1_\2', s)
    return s.lower()


def snake_to_camel(s: str) -> str:
    parts = s.split('_')
    return parts[0] + ''.join(p.capitalize() for p in parts[1:])


def count_sentences(s: str) -> int:
    return len(re.findall(r'[.!?]+', s))


def count_paragraphs(s: str) -> int:
    paragraphs = [p.strip() for p in s.split('\n\n') if p.strip()]
    return len(paragraphs)


def is_valid_json(s: str) -> bool:
    try:
        json.loads(s)
        return True
    except (json.JSONDecodeError, ValueError):
        return False
