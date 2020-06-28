from app.models.recipe_phase import RecipePhase


def test_create_recipe_phase():
    recipe_phase = RecipePhase(1, 2, 3, 4, 5, 6)

    assert recipe_phase.recipe_id == 1
    assert recipe_phase.recipe_phase_num == 2
    assert recipe_phase.num_hours == 3
    assert recipe_phase.power_level == 4
    assert recipe_phase.red_level == 5
    assert recipe_phase.blue_level == 6


def test_create_recipe_phase_from_json():
    recipephase = RecipePhase.from_json(
        {"recipe_id": 1, "recipe_phase_num": 2, "num_hours": 3, "power_level": 4, "red_level": 5, "blue_level": 6})

    assert recipephase.recipe_id == 1
    assert recipephase.recipe_phase_num == 2
    assert recipephase.num_hours == 3
    assert recipephase.power_level == 4
    assert recipephase.red_level == 5
    assert recipephase.blue_level == 6
