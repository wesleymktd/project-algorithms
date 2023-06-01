def study_schedule(permanence_period, target_time):
    count = 0
    if target_time == "" or not target_time or not permanence_period:
        return None

    # if not permanence_period:
    #     return None

    for period in permanence_period:
        if (
            not isinstance(period[0], int)
            or not isinstance(period[1], int)
            or len(period) != 2
        ):
            return None

        start_period, finally_period = period

        if start_period <= target_time <= finally_period:
            count += 1

    return count


# estudante             1       2       3       4       5       6
# permanence_period = [(5, 2), (1, 2), (2, 3), (1, 5), (4, 5), (4, 5)]
# print(study_schedule(permanence_period, 1))
# esse algoritmo vai percorrer todas as tu
