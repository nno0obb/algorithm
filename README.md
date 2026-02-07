# algorithm-boj

# Redo

## leetcode

- [316. Remove Duplicate Letters](https://leetcode.com/problems/remove-duplicate-letters)
- [332. Reconstruct Itinerary](https://leetcode.com/problems/reconstruct-itinerary/description/)
- [336. Palindrome Pairs](https://leetcode.com/problems/palindrome-pairs/description/)
- [239. Sliding Window Maximum](https://leetcode.com/problems/sliding-window-maximum/description/)
- [76. Minimum Window Substring](https://leetcode.com/problems/minimum-window-substring/description/)
- [424. Longest Repeating Character Replacement](https://leetcode.com/problems/longest-repeating-character-replacement/)
- [406. Queue Reconstruction by Height](https://leetcode.com/problems/queue-reconstruction-by-height/description/)
- [621. Task Scheduler](https://leetcode.com/problems/task-scheduler/)
- [134. Gas Station](https://leetcode.com/problems/gas-station/description/)


## boj

- [25918. 북극곰은 괄호를 찢어](https://www.acmicpc.net/problem/25918)
- [22342. 계산 로봇](https://www.acmicpc.net/problem/22342)
- [9764. 서로 다른 자연수의 합](https://www.acmicpc.net/problem/9764)
- [1377. 버블 소트](https://www.acmicpc.net/problem/1377)
- [1517. 버블 소트](https://www.acmicpc.net/problem/1517)
- [13023. ABCDE](https://www.acmicpc.net/problem/13023)
- [4307. 개미](https://www.acmicpc.net/problem/4307)
- [1300. K번째 수](https://www.acmicpc.net/problem/1300)
- [1744. 수 묶기](https://www.acmicpc.net/problem/1744)
- [1456. 거의 소수](https://www.acmicpc.net/problem/1456)
- [1016. 제곱 ㄴㄴ수](https://www.acmicpc.net/problem/1016)
- [1850. 칵테일](https://www.acmicpc.net/problem/1033https://www.acmicpc.net/problem/1033)
- [1334. 다음 팰린드롬 수](https://www.acmicpc.net/problem/1334)
- [1325. 효율적인 해킹](https://www.acmicpc.net/problem/1325)
- [1043. 거짓말](https://www.acmicpc.net/problem/1043)
- [1854. K번째 최단경로 찾기](https://www.acmicpc.net/problem/1854)
- [1219. 오민식의 고민](https://www.acmicpc.net/problem/1219)
- [11505. 구간 곱 구하기](https://www.acmicpc.net/problem/11505)
- [1722. 순열의 순서](https://www.acmicpc.net/problem/1722)
- [1256. 사전](https://www.acmicpc.net/problem/1256)
- [1947. 선물 전달](https://www.acmicpc.net/problem/1947)
- [11049. 행렬 곱셈 순서](https://www.acmicpc.net/problem/11049)

# Init

## boj

```shell
$ activate
$ cd problem_solving/boj
$ python3 init.py --no <NO>
```

# Test

## boj

### pytho기

```shell
$ activate
$ cd problem_solving/boj
$ cat <NO>/inputs/input1 | python3 <NO>/soln<NO>.py
$ pytest runcase.py -v --no <NO>
$ pytest runcase.py -v --no <NO> --relative-error "10**-2"
```

## leetcode

```shell
$ activate
$ cd problem_solving/leetcode
$ pytest sol<NO>.py -v
```

# ETC

## boj

### obsidian

```shell
$ activate
$ cd problem_solving/boj
$ python3 obsidian.py --no <NO>
```
