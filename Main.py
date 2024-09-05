from ShapeWarehouse import ShapeWarehouse


def main():
    my_container = ShapeWarehouse(['Green', 'Blue', 'Red', 'Yellow'], [1, 2, 3, 4, 5])

    # Generate 100 shapes
    my_container.generate(100)

    # Output the results
    print("total area:", my_container.sum_areas())
    print("total perimeter:", my_container.sum_perimeters())
    print("colors:", my_container.count_colors())


if __name__ == '__main__':
    main()
# Assertions
    assert_container = ShapeWarehouse(['Green', 'Blue', 'Red', 'Yellow'], [1, 2, 3, 4, 5])
    assert_container.generate(100)
    assert assert_container.sum_areas() > 0, "Total area should be greater than 0"
    assert assert_container.sum_perimeters() > 0, "Total perimeter should be greater than 0"
    assert isinstance(assert_container.count_colors(), dict), "Color counts should be a dictionary"
    assert sum(assert_container.count_colors().values()) == 100, "The total number of shapes should be 100"
    assert all(count >= 0 for count in assert_container.count_colors().values()), ("Each color "
                                                                                   "count should be non-negative")
