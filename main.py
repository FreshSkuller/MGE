import math

wheel_increase = 500

class WheelCounter:
    def __init__(self, current_amount, target_amount, midas_hand_threshold):
        self.current_amount = current_amount
        self.target_amount = target_amount
        self.midas_hand_threshold = midas_hand_threshold

    def calculate_wheels(self):
        # Считаем количество колес до достижения целевой суммы
        total_wheels = (self.target_amount - 1) // wheel_increase
        
        # Номер колеса выпадения мидаса
        wheel_midas = ((self.midas_hand_threshold + 1) // wheel_increase)
        
        # Всего собрано средств без допа
        buf_sum_target = (total_wheels * self.target_amount // 2)
        
        # Всего собрано средств
        sum_target = buf_sum_target + self.current_amount
        
        # Количество колес, необходимых для вычитания мидаса
        remain_wheel_midas = 3
        
        if wheel_midas == total_wheels:
            remaining_sum = self.current_amount - remain_wheel_midas * 1500
            # Корректируем оставшуюся сумму, учитывая мидас
            while remaining_sum < 0 and remain_wheel_midas > 0:
                remain_wheel_midas -= 1
                remaining_sum = self.current_amount - remain_wheel_midas * 1500
            # Осталось колес
            buf_wheels_left = remain_wheel_midas
        else:
            remaining_sum = sum_target - remain_wheel_midas * 1500
            
            # Корректируем оставшуюся сумму, учитывая мидас
            while remaining_sum < 0 and remain_wheel_midas > 0:
                remain_wheel_midas -= 1
                remaining_sum = sum_target - remain_wheel_midas * 1500
            # Осталось колес
            buf_wheels_left = int(math.floor((-1 + math.sqrt(1 + 4 * (remaining_sum / (wheel_increase / 2)))) / 2))
        
        # Осталось мидасов
        left_midas = 3 - remain_wheel_midas
        
        if left_midas > 0:
            new_target = 1500
            # Остаток до сбора
            new_target_amount = remaining_sum
            # Считаем количество колес до достижения новой целевой суммы
            new_total_wheels = total_wheels
        else:
            new_target = wheel_increase + (buf_wheels_left * wheel_increase)
            sequence_sum = sum(range(wheel_increase, new_target, wheel_increase))
            # Остаток до сбора
            new_target_amount = remaining_sum - sequence_sum
            # Считаем количество колес до достижения новой целевой суммы
            new_total_wheels = (new_target - 1) // wheel_increase
        
        # Всего колес с учетом мидаса
        total_wheels_midas = new_total_wheels + remain_wheel_midas
        
        # Количество оставшихся колес после мидаса
        wheels_left = total_wheels_midas - wheel_midas

        return total_wheels, wheel_midas, total_wheels_midas, wheels_left, left_midas, new_target_amount, new_target

def get_input(prompt):
    while True:
        try:
            value = int(input(prompt))
            if value < 0:
                raise ValueError("Значение должно быть положительным.")
            return value
        except ValueError as e:
            print(f"Неверный ввод: {e}. Попробуйте снова.")

def main():
    print("Добро пожаловать в программу подсчета колёс и сбора после руки Мидаса.")
    current_amount = get_input("Введите текущее количество денег на сборе: ")
    target_amount = get_input("Введите текущую сумму сбора: ")
    midas_hand_threshold = get_input("Введите сумму, при которой выпала рука мидаса (например, 1000): ")

    counter = WheelCounter(current_amount, target_amount, midas_hand_threshold)
    total_wheels, wheel_midas, total_wheels_midas, wheels_left, left_midas, new_target_amount, new_target = counter.calculate_wheels()

    print(f"\nРезультаты расчета:")
    print(f"Изначально количество колес: {total_wheels}")
    print(f"Номер колеса на котором выпал мидас: {wheel_midas}")
    print(f"Общее количество колес вместе с мидасом: {total_wheels_midas}")
    print(f"Количество оставшихся колес вместе с мидасом: {wheels_left}")
    print(f"Мидаса осталось: {left_midas}")
    print(f"Новый сбор после мидаса: {new_target_amount} из {new_target}")

if __name__ == "__main__":
    main()
