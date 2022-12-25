def find_pairs(arr, target_sum):
 pairs = set()
 for i in range(len(arr)):
   diff = target_sum - arr[i]
   if diff in arr and diff != arr[i]:
     pairs.add((arr[i], diff))
 return pairs
print(find_pairs([1,2,3,4,5],5))
print(find_pairs([1,2,3,4,5],6))
print(find_pairs([1,2,3,4,5],7))
print(find_pairs([1,2,3,4,5],8))
          
