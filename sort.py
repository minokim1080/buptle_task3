# 병합 정렬을 구현한 메소드입니다.
def merge_sort(arr):
    if len(arr) <= 1:
        return arr

    # 리스트를 반으로 분할
    mid = len(arr) // 2
    left = arr[:mid]
    right = arr[mid:]

    # 정복. 분할된 리스트들을 재귀적으로 정렬
    left = merge_sort(left)
    right = merge_sort(right)

    # 정렬된 리스트들을 병합
    return _merge(left, right)


# 병합을 구현한 메소드입니다. 병합 정렬 내부에서 사용합니다.
def _merge(left, right):
    result = []
    i = j = 0

    # 두 부분 리스트를 비교하면서 작은 원소를 순서대로 병합
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            result.append(left[i])
            i += 1
            continue

        result.append(right[j])
        j += 1

    # 남은 원소들을 결과 리스트에 추가
    result.extend(left[i:])
    result.extend(right[j:])

    return result

# 퀵 정렬을 구현한 메소드입니다.
def quick_sort(arr):
    print("start_new")

    if len(arr) <= 1:
        return arr

    # 최악의 성능을 방지하기 위해 3개의 pivot 후보군 중 중간 값을 선택합니다.
    pivot_candidates = [arr[0], arr[len(arr) // 2], arr[-1]]
    pivot = _find_middle_value(pivot_candidates[0], pivot_candidates[1], pivot_candidates[2])
    left, equal, right = [], [], []

    for num in arr:
        if num < pivot:
            left.append(num)
        elif num == pivot:
            equal.append(num)
        else:
            right.append(num)

    print("equal : " + str(equal))
    print("left : " + str(left))
    print("right : " + str(right))

    return quick_sort(left) + equal + quick_sort(right)


# 매개 변수로 받은 세 값 중 중간 값을 찾는 메소드입니다.
def _find_middle_value(a, b, c):
    if (a <= b <= c) or (c <= b <= a):
        return b

    if (b <= a <= c) or (c <= a <= b):
        return a

    return c
