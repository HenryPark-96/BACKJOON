### map()

- 여러 개의 데이터를 한 번에 다른 형태로 변화하기 위해서 사용된다.
- map()함수는 두번째 인자로 넘어온 데이터가 담고 있는 모든 데이터에 변환 함수를 적용하여 다른 형태의 데이터를 반환한다.

```python
map(반환 함수, 순위 가능한 데이터)

# 입력으로 받은 값들을 int값으로 가져온다.
num_1, num_2 = map(int, input().split())
```

