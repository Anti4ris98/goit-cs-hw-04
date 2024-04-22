import matplotlib.pyplot as plt
import numpy as np

# Оголошуємо символьні змінні
x = np.linspace(0, 30, 100)  # Виберіть потрібний діапазон x
e = np.exp(1)

# Задаємо формулу
formula = 2 * (4 / (1.2 * np.sqrt(2 * np.pi)) * np.power(np.power(e, -0.5 * 40 * (x - 11) / 1.2 * 41), 2) +
               7 / (2.4 * np.sqrt(2 * np.pi)) * np.power(np.power(e, -0.5 * 40 * (x - 15) / 2.4 * 41), 2))

# Візуалізуємо формулу
plt.plot(x, formula, label=r'$2 \left( \frac{4}{1.2\sqrt{2\pi}} \left( e^{-\frac{1}{2} \cdot 40 \cdot \frac{x-11}{1.2} \cdot 41} \right)^2 + \frac{7}{2.4\sqrt{2\pi}} \left( e^{-\frac{1}{2} \cdot 40 \cdot \frac{x-15}{2.4} \cdot 41} \right)^2 \right)$')

# Додаткові налаштування, якщо потрібно
plt.xlabel('x')
plt.ylabel('Formula Value')
plt.title('Formula Visualization')
plt.legend()
plt.show()