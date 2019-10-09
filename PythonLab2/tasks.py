def string_times(str, n):
  return str*n
def front_times(str, n):
  return str*n if len(str)<3 else str[0:3]*n
def string_bits(stri):
  return (str([stri[i] for i in range(len(stri)) if i%2==0])).replace(", ", "").replace("\'","")[1:-1]
def string_splosion(stri):
  return stri[0]+(str([stri[0:i]+stri[i] for i in range(len(stri)) if i>0]).replace(", ", "").replace("\'","")[1:-1])
def last2(str):
    return len([str[i]+str[i+1] for i in range(0, len(str[:-2])) if (str[i]+str[i+1]==str[-2:])])
def array_count9(nums):
  return str(nums).count("9")
def array_front9(nums):
  return nums.index(9)<4 if 9 in nums else False
def array123(nums):
  return True if (str(nums)).count("1, 2, 3")>0 else False
def string_match(a, b):
  return(len([a[i] for i in range(min(len(a), len(b))-1) if a[i]==b[i] and a[i+1]==b[i+1]]))
def make_bricks(small, big, goal):
  return ((goal//5)<=big and goal%((goal//5)*5)<=small) or ((goal//5)<=big+small//5 and goal%(5*(goal//5))<=small%5) or small>=goal or (goal-5*big<=small and goal-5*big>0)
def lone_sum(a, b, c):
  return sum({a,b,c}) if len({a,b,c})==3 else sum({a,b,c})-a if a==b or a==c else sum({a,b,c})-b
def lucky_sum(a, b, c):
  return sum([a, b, c]) if 13 not in [a, b, c] else 0 if a==13 else a if b==13 else a+b
def no_teen_sum(a, b, c):
  return sum([a if a<13 or a==15 or a==16 or a>19 else 0,b if b<13 or b==15 or b==16 or b>19 else 0,c if c<13 or c==15 or c==16 or c>19 else 0])
def round_sum(a, b, c):
  return int(round(a if (a-5)%10!=0 else a+5 , -1)+round(b if (b-5)%10!=0 else b+5 , -1)+round(c if (c-5)%10!=0 else c+5, -1))  
def close_far(a, b, c):
   return abs(abs(a-b)+abs(b-c)+abs(a-c))>=5 if a!=c and a!=b and b!=c else abs(abs(a-b)+abs(b-c)+abs(a-c))>=4
def make_chocolate(small, big, goal):
  return goal-5*big if 0<=goal-5*big<=small else goal%((goal//5)*5) if (goal//5>0 and (goal//5)<=big and goal%((goal//5)*5)<=small) else (small//5)*5+goal%(5*(goal//5))-((big+small//5)%(goal//5))*5 if (goal//5>0 and (goal//5)<=big+small//5 and goal%(5*(goal//5))<=small%5) else goal if small>=goal else goal-5*big if (goal-5*big<=small and goal-5*big>0) else -1
def double_char(stri):
  return "".join([stri[i//2] for i in range(0, len(stri)*2)])
def count_hi(str):
  return str.count("hi")
def cat_dog(str):
  return str.count("cat")==str.count("dog")
def count_code(str):
  return len([i for i in range(0, len(str)-3) if str[i]=='c' and str[i+1]=='o' and str[i+3]=='e'])
def end_other(a, b):
  return a[-len(b) :].lower()==b.lower() or b[-len(a) :].lower()==a.lower()
def xyz_there(str):
  return str.count("xyz")-str.count(".xyz")>0 if "xyz" in str else False
def count_evens(nums):
  return str([i%2 for i in nums]).count("0")
def big_diff(nums):
  return max(nums)-min(nums)
def centered_average(nums):
  return (sum(nums)-min(nums)-max(nums))//(len(nums)-2)
def sum13(nums):
  return sum([nums[i] for i in range(len(nums)) if(nums[i]!=13 and (i==0 or nums[i-1]!=13))])
def sum67(nums):
  k=True
  sum=0
  for i in range(len(nums)): 
    k=True
    sum=0
    for i in range(len(nums)): 
      if k and nums[i]!=6:
        sum+=nums[i]
      elif nums[i]==6:
        k=False
      elif not k and nums[i]==7:
        k=True
  return sum
def has22(nums):


  return len([nums[i] for i in range(1, len(nums)-1) if nums[i]==nums[i-1]==2 or nums[i]==nums[i+1]==2])>0 if len(nums)!=2 else nums[0]==nums[1]==2
