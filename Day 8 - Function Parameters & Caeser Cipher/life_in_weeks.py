def life_in_weeks(age):
    max_life_span = 90
    total_weeks_in_a_year = 52
    total_weeks = max_life_span * total_weeks_in_a_year

    remaining_weeks = total_weeks - (age * total_weeks_in_a_year)

    print(f"You have {remaining_weeks} weeks left.")

life_in_weeks(30)