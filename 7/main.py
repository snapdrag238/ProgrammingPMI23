import sys
import math
import matplotlib.pyplot as plt

# Забезпечення коректного виведення UTF-8 в консолі Windows
if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8")

try:
    import ipywidgets as widgets
    from IPython.display import display
    HAS_WIDGETS = True
except ImportError:
    HAS_WIDGETS = False


def _validate_inputs(n, r, rotation=0.0):
    """
    Перевірка вхідних даних:
    - n — ціле число >= 3
    - r — число > 0
    - rotation — число
    """
    if not isinstance(n, int) or isinstance(n, bool):
        raise TypeError("n має бути цілим числом")
    if n < 3:
        raise ValueError("n має бути не менше 3")

    if not isinstance(r, (int, float)) or isinstance(r, bool):
        raise TypeError("r має бути числом")
    if r <= 0:
        raise ValueError("r має бути додатним")

    if not isinstance(rotation, (int, float)) or isinstance(rotation, bool):
        raise TypeError("rotation має бути числом")


def polygon(n: int, r=1.0, rotation=0.0) -> list:
    """
    Повертає список координат вершин правильного n-кутника,
    вписаного в коло радіуса r (округлення до 3 знаків).
    """
    _validate_inputs(n, r, rotation)

    vertices = []
    angle_step = 2.0 * math.pi / n
    for i in range(n):
        angle = rotation + i * angle_step
        x = round(r * math.cos(angle), 3) + 0.0
        y = round(r * math.sin(angle), 3) + 0.0
        vertices.append((x, y))
    return vertices


def perimeter(n: int, r=1.0) -> float:
    """
    Повертає периметр n-кутника з округленням до 4 знаків.
    """
    if not isinstance(n, int) or isinstance(n, bool):
        raise TypeError("n має бути цілим числом")
    if n < 3:
        raise ValueError("n має бути не менше 3")

    if not isinstance(r, (int, float)) or isinstance(r, bool):
        raise TypeError("r має бути числом")
    if r <= 0:
        raise ValueError("r має бути додатним")

    # Довжина сторони: a = 2 * r * sin(pi / n); P = n * a
    p = 2.0 * n * r * math.sin(math.pi / n)
    return round(p, 4)


def plot_polygon(n: int, r=1.0, color="navy"):
    """
    Створює фігуру через plt.subplots(...), зафарбовує многокутник,
    позначає вершини, малює описане коло пунктиром, встановлює однаковий
    масштаб осей і порівнює в заголовку периметр із 2*pi*r.
    Повертає пару (fig, ax); plt.show() у ній не викликається.
    """
    _validate_inputs(n, r)

    verts = polygon(n, r)
    xs = [v[0] for v in verts]
    ys = [v[1] for v in verts]

    fig, ax = plt.subplots(figsize=(6, 6))

    # Пунктирна лінія описаного кола
    num_circle_pts = 200
    circle_theta = [2 * math.pi * i / num_circle_pts for i in range(num_circle_pts + 1)]
    cx = [r * math.cos(t) for t in circle_theta]
    cy = [r * math.sin(t) for t in circle_theta]
    ax.plot(cx, cy, linestyle="--", color="gray", label="Описане коло")

    # Зафарбовування многокутника (fill)
    closed_xs = xs + [xs[0]]
    closed_ys = ys + [ys[0]]
    ax.fill(closed_xs, closed_ys, color=color, alpha=0.3, label=f"{n}-кутник")
    ax.plot(closed_xs, closed_ys, color=color, linewidth=2)

    # Вершини через scatter
    ax.scatter(xs, ys, color=color, s=40, zorder=5)

    # Однаковий масштаб осей
    ax.set_aspect("equal")

    # Порівняння в заголовку периметра із 2*pi*r
    p_val = perimeter(n, r)
    circ_val = round(2 * math.pi * r, 4)
    ax.set_title(f"n = {n}: P = {p_val}, 2πr = {circ_val}")

    margin = r * 1.25
    ax.set_xlim(-margin, margin)
    ax.set_ylim(-margin, margin)
    ax.grid(True, linestyle=":", alpha=0.5)
    ax.legend(loc="upper right")

    return fig, ax


def make_ui():
    """
    Будує інтерфейс на ipywidgets і повертає кореневий віджет.
    Графік і повідомлення виводяться у віджет Output.
    Некоректне значення у полі показує «Помилка: пояснення».
    """
    if not HAS_WIDGETS:
        raise RuntimeError("Для використання make_ui необхідні бібліотеки ipywidgets та IPython.")

    n_slider = widgets.IntSlider(value=6, min=3, max=30, step=1, description="n:")
    r_slider = widgets.FloatSlider(value=1.0, min=0.1, max=10.0, step=0.1, description="r:")
    color_picker = widgets.ColorPicker(value="#000080", description="Колір:")
    out = widgets.Output()

    def update(*args):
        out.clear_output(wait=True)
        with out:
            try:
                fig, ax = plot_polygon(n_slider.value, r_slider.value, color=color_picker.value)
                display(fig)
                plt.close(fig)
            except Exception as e:
                print(f"Помилка: {e}")

    n_slider.observe(update, names="value")
    r_slider.observe(update, names="value")
    color_picker.observe(update, names="value")

    # Початковий виклик для відображення графіка
    update()

    return widgets.VBox([
        widgets.HBox([n_slider, r_slider, color_picker]),
        out
    ])


if __name__ == "__main__":
    print("=== Перевірка прикладів з умови ===")
    print("polygon(4):")
    print(polygon(4))

    print("\nperimeter(6, 1), perimeter(1000, 1):")
    print(perimeter(6, 1), perimeter(1000, 1))

    fig, ax = plot_polygon(5)
    print("\nax.get_aspect(), ax.get_title():")
    print(ax.get_aspect(), repr(ax.get_title()))
    plt.close(fig)

    print("\nПеревірка винятків:")
    try:
        polygon(2)
    except ValueError as e:
        print("polygon(2) -> ValueError:", e)

    try:
        polygon(5, r=0)
    except ValueError as e:
        print("polygon(5, r=0) -> ValueError:", e)
