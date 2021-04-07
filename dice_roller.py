import random


def main():
    print('You rolled a die')
    print("adara")
    dice_rolls = int(input("你想掷几个骰子?"))
    dice_rolls = dice_rolls + 1
    dice_size = int(input("骰子有几面?"))
    dice_sum = 0
    # roll = 5
    for i in range(1, dice_rolls):
        dice_sum += 1
        print(f"这是第{i}次循环=================================")
        roll = random.randint(1, dice_size)
        print(f'You rolled a {roll}')
        if roll == 1:
            print(f"你筛选到了{roll}，这个是最小的！！")
        elif roll == 6:
            print(f"你筛选到了{roll}，Nice！！!这个是最大的！！")
        else:
            print("不大不小")
    print(f'You have rolled a total of {dice_sum}')


if __name__ == "__main__":
    main()
