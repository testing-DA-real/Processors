import csv
import json
import os
from typing import List, Dict, Any, Optional, Tuple, Generator
from collections import defaultdict, Counter
from datetime import datetime, date
import re


def read_csv(filepath: str) -> List[Dict[str, str]]:
    results = []
    with open(filepath, 'r', newline='', encoding='utf-8') as f:
        reader = csv.DictReader(f)
        for row in reader:
            results.append(row)
    return results


def write_csv(filepath: str, data: List[Dict[str, Any]]) -> None:
    if not data:
        return
    with open(filepath, 'w', newline='', encoding='utf-8') as f:
        writer = csv.DictWriter(f, fieldnames=list(data[0].keys()))
        writer.writeheader()
        writer.writerows(data)


def read_json(filepath: str) -> Any:
    with open(filepath, 'r', encoding='utf-8') as f:
        return json.load(f)


def write_json(filepath: str, data: Any, indent: int = 2) -> None:
    with open(filepath, 'w', encoding='utf-8') as f:
        json.dump(data, f, indent=indent, ensure_ascii=False)


def read_lines(filepath: str) -> List[str]:
    with open(filepath, 'r', encoding='utf-8') as f:
        return [line.rstrip('\n') for line in f]


def write_lines(filepath: str, lines: List[str]) -> None:
    with open(filepath, 'w', encoding='utf-8') as f:
        for line in lines:
            f.write(line + '\n')


def append_line(filepath: str, line: str) -> None:
    with open(filepath, 'a', encoding='utf-8') as f:
        f.write(line + '\n')


def file_exists(filepath: str) -> bool:
    return os.path.exists(filepath)


def file_size(filepath: str) -> int:
    return os.path.getsize(filepath)


def get_file_extension(filepath: str) -> str:
    _, ext = os.path.splitext(filepath)
    return ext.lower()


def chunk_list(data: List[Any], chunk_size: int) -> Generator[List[Any], None, None]:
    for i in range(0, len(data), chunk_size):
        yield data[i:i + chunk_size]


def flatten(nested_list: List[List[Any]]) -> List[Any]:
    return [item for sublist in nested_list for item in sublist]


def unique_by_key(items: List[Dict], key: str) -> List[Dict]:
    seen = set()
    result = []
    for item in items:
        val = item.get(key)
        if val not in seen:
            seen.add(val)
            result.append(item)
    return result


def group_by(items: List[Dict], key: str) -> Dict[Any, List[Dict]]:
    groups = defaultdict(list)
    for item in items:
        groups[item.get(key)].append(item)
    return dict(groups)


def sort_by_key(items: List[Dict], key: str, reverse: bool = False) -> List[Dict]:
    return sorted(items, key=lambda x: x.get(key, ''), reverse=reverse)


def filter_by_value(items: List[Dict], key: str, value: Any) -> List[Dict]:
    return [item for item in items if item.get(key) == value]


def merge_dicts(d1: Dict, d2: Dict, overwrite: bool = True) -> Dict:
    merged = d1.copy()
    for k, v in d2.items():
        if overwrite or k not in merged:
            merged[k] = v
    return merged


def deep_merge(base: Dict, override: Dict) -> Dict:
    result = base.copy()
    for key, value in override.items():
        if key in result and isinstance(result[key], dict) and isinstance(value, dict):
            result[key] = deep_merge(result[key], value)
        else:
            result[key] = value
    return result


def paginate(items: List[Any], page: int, per_page: int) -> Tuple[List[Any], Dict]:
    total = len(items)
    total_pages = max(1, (total + per_page - 1) // per_page)
    start = (page - 1) * per_page
    end = start + per_page
    page_items = items[start:end]
    meta = {
        'page': page,
        'per_page': per_page,
        'total': total,
        'total_pages': total_pages,
        'has_next': page < total_pages,
        'has_prev': page > 1,
    }
    return page_items, meta


def parse_date(date_str: str, formats: Optional[List[str]] = None) -> Optional[date]:
    if formats is None:
        formats = ['%Y-%m-%d', '%d/%m/%Y', '%m/%d/%Y', '%Y/%m/%d']
    for fmt in formats:
        try:
            return datetime.strptime(date_str, fmt).date()
        except ValueError:
            continue
    return None


def format_date(d: date, fmt: str = '%Y-%m-%d') -> str:
    return d.strftime(fmt)


def days_between(d1: date, d2: date) -> int:
    return abs((d2 - d1).days)


def is_weekend(d: date) -> bool:
    return d.weekday() >= 5


def is_weekday(d: date) -> bool:
    return d.weekday() < 5


def get_age(birth_date: date) -> int:
    today = date.today()
    age = today.year - birth_date.year
    if (today.month, today.day) < (birth_date.month, birth_date.day):
        age -= 1
    return age


def celsius_to_fahrenheit(c: float) -> float:
    return (c * 9 / 5) + 32


def fahrenheit_to_celsius(f: float) -> float:
    return (f - 32) * 5 / 9


def kg_to_lbs(kg: float) -> float:
    return kg * 2.20462


def lbs_to_kg(lbs: float) -> float:
    return lbs / 2.20462


def km_to_miles(km: float) -> float:
    return km * 0.621371


def miles_to_km(miles: float) -> float:
    return miles / 0.621371


def safe_get(data: Dict, *keys, default=None):
    current = data
    for key in keys:
        if isinstance(current, dict):
            current = current.get(key)
            if current is None:
                return default
        else:
            return default
    return current


def deep_find(data: Dict, key: str) -> List[Any]:
    results = []
    if isinstance(data, dict):
        for k, v in data.items():
            if k == key:
                results.append(v)
            if isinstance(v, (dict, list)):
                results.extend(deep_find(v, key))
    elif isinstance(data, list):
        for item in data:
            results.extend(deep_find(item, key))
    return results


def sanitize_filename(name: str) -> str:
    name = re.sub(r'[<>:"/\\|?*]', '_', name)
    name = re.sub(r'\s+', '_', name)
    return name.strip('_.')


def generate_id(prefix: str = '', length: int = 8) -> str:
    import random
    import string
    chars = string.ascii_lowercase + string.digits
    suffix = ''.join(random.choice(chars) for _ in range(length))
    return f"{prefix}{suffix}"


def rate_limit(max_calls: int, period: float):
    import time
    calls = []
    def wrapper(func):
        def inner(*args, **kwargs):
            now = time.time()
            nonlocal calls
            calls = [c for c in calls if now - c < period]
            if len(calls) >= max_calls:
                raise RuntimeError(f"Rate limit exceeded: max {max_calls} calls per {period}s")
            calls.append(now)
            return func(*args, **kwargs)
        return inner
    return wrapper


def retry(max_attempts: int = 3, delay: float = 1.0):
    import time
    def decorator(func):
        def wrapper(*args, **kwargs):
            last_exc = None
            for attempt in range(1, max_attempts + 1):
                try:
                    return func(*args, **kwargs)
                except Exception as e:
                    last_exc = e
                    if attempt < max_attempts:
                        time.sleep(delay)
            raise last_exc
        return wrapper
    return decorator


def timed(func):
    import time
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        elapsed = time.time() - start
        print(f"{func.__name__} took {elapsed:.4f}s")
        return result
    return wrapper


def batch_process(items: List[Any], batch_size: int, processor) -> List[Any]:
    results = []
    for batch in chunk_list(items, batch_size):
        results.extend(processor(batch))
    return results


def compare_lists(list1: List, list2: List) -> Dict:
    set1, set2 = set(list1), set(list2)
    return {
        'added': list(set2 - set1),
        'removed': list(set1 - set2),
        'common': list(set1 & set2),
    }


def deduplicate(items: List[Any]) -> List[Any]:
    seen = set()
    result = []
    for item in items:
        if item not in seen:
            seen.add(item)
            result.append(item)
    return result


def interleave(*lists) -> List[Any]:
    result = []
    max_len = max(len(lst) for lst in lists)
    for i in range(max_len):
        for lst in lists:
            if i < len(lst):
                result.append(lst[i])
    return result


def windowed(items: List[Any], window_size: int) -> Generator[Tuple, None, None]:
    for i in range(len(items) - window_size + 1):
        yield tuple(items[i:i + window_size])


def rotate_left(items: List[Any], n: int) -> List[Any]:
    if not items:
        return items
    n = n % len(items)
    return items[n:] + items[:n]


def rotate_right(items: List[Any], n: int) -> List[Any]:
    if not items:
        return items
    n = n % len(items)
    return items[-n:] + items[:-n]


def to_query_string(params: Dict[str, str]) -> str:
    return '&'.join(f"{k}={v}" for k, v in params.items())


def parse_query_string(qs: str) -> Dict[str, str]:
    params = {}
    for part in qs.split('&'):
        if '=' in part:
            k, v = part.split('=', 1)
            params[k] = v
    return params


def approximate_equals(a: float, b: float, epsilon: float = 1e-9) -> bool:
    return abs(a - b) < epsilon


def weighted_sample(items: List[Any], weights: List[float], k: int = 1) -> List[Any]:
    import random
    if len(items) != len(weights):
        raise ValueError("Items and weights must have same length")
    total = sum(weights)
    probs = [w / total for w in weights]
    return random.choices(items, weights=probs, k=k)


def shuffle_preserve_order(original: List[Any], reference: List[Any]) -> List[Any]:
    order = {v: i for i, v in enumerate(reference)}
    return sorted(original, key=lambda x: order.get(x, len(reference)))


def to_table(data: List[Dict[str, Any]]) -> str:
    if not data:
        return ''
    headers = list(data[0].keys())
    col_widths = {h: len(h) for h in headers}
    for row in data:
        for h in headers:
            col_widths[h] = max(col_widths[h], len(str(row.get(h, ''))))
    sep = '+' + '+'.join('-' * (col_widths[h] + 2) for h in headers) + '+'
    header_row = '| ' + ' | '.join(h.ljust(col_widths[h]) for h in headers) + ' |'
    lines = [sep, header_row, sep]
    for row in data:
        vals = [str(row.get(h, '')).ljust(col_widths[h]) for h in headers]
        lines.append('| ' + ' | '.join(vals) + ' |')
    lines.append(sep)
    return '\n'.join(lines)
