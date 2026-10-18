import pytest
from shapes import Shape, Cube, Rectangle, Cylinder, Sphere


def test_sphere():
    sphere = Sphere(5)
    assert sphere.calculate_area() == pytest.approx(314.159, abs=0.001)
    assert sphere.calculate_volume() == pytest.approx(523.599, abs=0.001)


def test_cube():
    cube = Cube(3)
    assert cube.calculate_area() == pytest.approx(54)
    assert cube.calculate_volume() == pytest.approx(27)


def test_rectangle():
    rect = Rectangle(4, 5)
    assert rect.calculate_area() == pytest.approx(20)
    assert rect.calculate_volume() == 0


def test_cylinder():
    cyl = Cylinder(2, 5)
    assert cyl.calculate_area() == pytest.approx(87.965, abs=0.001)
    assert cyl.calculate_volume() == pytest.approx(62.832, abs=0.001)


@pytest.mark.parametrize("shape", [Cube(0), Rectangle(0, 0), Cylinder(0, 0), Sphere(0)])
def test_zero_dimensions(shape):
    assert shape.calculate_area() == 0
    assert shape.calculate_volume() == 0


def test_shape_is_abstract():
    with pytest.raises(TypeError):
        Shape()