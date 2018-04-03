def get_querys():
    calls = int(raw_input())
    querys = []
    for _ in calls:
        querys.append(map(int,raw_input().split()))
    return querys

def getLuckyNums(maximum):
    if maximum < 4:
        return []
    elif maximum < 7:
        return [4]
    else:
        lists = [4,7]
        ptr = 0
        while True:
            length = len(lists)
            for i in range(ptr,length):
                if lists[i]*10 + 4 <= maximum:
                    lists.append(lists[i]*10 + 4)
                if lists[i]*10 + 7 <= maximum:
                    lists.append(lists[i]*10 + 7)
            if len(lists) == length:
                break
            ptr = length
        return lists#sorted(lists)

def binarySearch(nums, target):
    if len(nums) == 0:
        return False, -1
    start = 0
    end = len(nums) - 1
    while start + 1 < end:
        mid = (start + end)//2
        if nums[mid] > target:
            end = mid
        elif nums[mid] < target:
            start = mid
        else:
            return True, mid
    if nums[start] == target:
        return True, start
    elif nums[end] == target:
        return True, end
    elif nums[end] < target:
        return False, end
    elif nums[start] < target:
        return False, start
    else:
        return False, -1

def SuperLuckyNums(querys):
    maximum = max(pair[-1] for pair in querys)
    luckyNums = getLuckyNums(maximum)
    base = set()
    def dfs(sln, luckyNums, maximum):
        if sln in base:
            return
        else:
            if sln != 1:
                base.add(sln)
            for num in luckyNums:
                if num*sln > maximum:
                    return
                else:
                    dfs(num*sln,luckyNums, maximum)
    if len(luckyNums) > 0:
        dfs(1,luckyNums,maximum)
    base = sorted(list(base))
    answers = []
    for start, end in querys:
        if start == end:
            answers.append(int(binarySearch(base,start)[0]))
        else:
            judge_start, idx_start = binarySearch(base,start)
            judge_end, idx_end = binarySearch(base,end)
            answers.append(int(((idx_end - idx_start + 1) + judge_start - 1)))
    return answers

if __name__ == "__main__":
    #read querys from input
    #returns count of super-lucky nubmers in intervals
    #lucky numbers is defined as numbers with digits 4 or 7 only
    #super-lucky numbers is defined as numbers that is product of lucky numbers or lucky number itself
    answers = SuperLuckyNums([[1,2],[47,47],[1,100]])
    for ans in answers:
        print(ans)