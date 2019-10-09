#Warmup-1
def sleep_in(weekday, vacation):
  return weekday==False or vacation==True
def monkey_trouble(a_smile, b_smile):
  return (a_smile==True and b_smile==True)or(a_smile==False and b_smile==False)

def sum_double(a, b):
  return a*4 if a==b else a+b
def diff21(n):
  return abs(n-21)*2 if n>21 else abs(n-21)
def parrot_trouble(talking, hour):
  return talking and (hour<7 or hour>20)
def makes10(a, b):
  return a == 10 or b == 10 or a+b==10
def near_hundred(n):
  return abs(n-100)<=10 or abs(n-200)<=10
def pos_neg(a, b, negative):
  return ((a<0 or b<0) and (a!=0 and b!=0) and not (a<0 and b<0) and not negative) or (negative and a<0 and b<0)
#String-1
def hello_name(name):
  return 'Hello '+name+'!'
def make_abba(a, b):
  return a+b+b+a
def make_tags(tag, word):
  return '<'+tag+'>'+word+'</'+tag+'>'
def make_out_word(out, word):
  return out[0:len(out)//2]+word+out[len(out)//2:]
def extra_end(str):
  return str[len(str)-2:]*3
def first_two(str):
  return str[0:2] if len(str)>2 else str
def first_half(str):
  return str[0:len(str)//2]
def without_end(str):
  return str[1:len(str)-1]
#List-1
def first_last6(nums):
  return str(nums[0])=='6' or str(nums[len(nums)-1])=='6' 
def same_first_last(nums):
  return len(nums)>=1 and nums[0]==nums[len(nums)-1]
def make_pi(num):
  return [3,1,4,1,5,9,2,6,5,3,5][0:num]
def common_end(a, b):
  return a[0]==b[0] or a[len(a)-1] == b[len(b)-1]
def sum3(nums):
  return sum(nums)
def rotate_left3(nums):
  return nums[1:]+nums[0:1]
def reverse3(nums):
  return nums[::-1]
def max_end3(nums):
  return nums[0:1]*len(nums) if nums[0]>nums[len(nums)-1] else nums[len(nums)-1:]*len(nums)
#Logic-1
def cigar_party(cigars, is_weekend):
  return (is_weekend and cigars>=40) or (cigars>=40 and cigars<=60)
def date_fashion(you, date):
  return 0 if (you>=8 or date>=8)and(you<=2 or date<=2) else 2 if (you>=8 or date>=8) else 0 if (you<=2 or date<=2) else 1
def squirrel_play(temp, is_summer):
  return (is_summer and 60<=temp<=100) or (60<=temp<=90)
def caught_speeding(speed, is_birthday):
  return 0 if is_birthday and speed<=65 else 1 if is_birthday and 66<=speed<=85 else 2 if is_birthday else 0 if speed<=60 else 1 if 61<=speed<=80 else 2
def sorta_sum(a, b):
  return 20 if 10<=a+b<=19 else a+b
def alarm_clock(day, vacation):
  return 'off' if vacation and (day==0 or day==6) else "10:00" if vacation else "10:00" if day==0 or day==6 else "7:00"
def love6(a, b):
  return a==6 or b==6 or a+b==6 or abs(a-b)==6
def in1to10(n, outside_mode):
  return (outside_mode and (n<=1 or n>=10)) or not outside_mode and 1<=n<=10


