def merge(left, right):
    merged_list = []
    i, j = 0, 0
    
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            merged_list.append(left[i])
            i += 1
        else:
            merged_list.append(right[j])
            j += 1

    merged_list.extend(left[i:])
    merged_list.extend(right[j:])
    
    return merged_list


def merge_sort(seq):
    if len(seq) > 1:
        mid = len(seq) // 2
        left_half = seq[:mid]
        right_half = seq[mid:]
        
        merge_sort(left_half)
        merge_sort(right_half)
        
        i = j = k = 0
        while i < len(left_half) and j < len(right_half):
            if left_half[i] < right_half[j]:
                seq[k] = left_half[i]
                i += 1
            else:
                seq[k] = right_half[j]
                j += 1
            k += 1
        
        while i < len(left_half):
            seq[k] = left_half[i]
            i += 1
            k += 1
        
        while j < len(right_half):
            seq[k] = right_half[j]
            j += 1
            k += 1


def merge_sort_iterative(seq):
    width = 1
    n = len(seq)
    while width < n:
        left = 0
        while left < n:
            right = min(left + 2 * width, n)
            mid = min(left + width, n)
            seq[left:right] = merge(seq[left:mid], seq[mid:right])
            left += 2 * width
        width *= 2
