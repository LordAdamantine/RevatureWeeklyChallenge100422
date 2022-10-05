def main():     # Separated like this for easy plug and play, can cycle through a list of lists if dealing with multiple entries
    print(interview([5, 5, 10, 10, 15, 15, 20, 20], 130))

def interview(scores, total):
    # First initialize the max times for each question considering the known format
    limits = [5, 5, 10, 10, 15, 15, 20, 20]
    
    # These were originally one if _ or _: block, but I split them for testing and liked it
    if (total > 120):      # Easy, run out of time? Fail!
        return "disqualified, ran out of time"
    if (len(scores) < 8):   # Easy, don't answer every question? Fail!
        return "disqualified, unanswered questions"

    # Now, we check each score one by one until one fails or they are shown to have passed them all
    i = 0
    while i < 8:    # Easy, score exceed the time limit for the question? Fail!
        if scores[i] > limits[i]:
            return f"disqualified, exceeded time limit on question {i + 1}"
        else:
            i += 1

    # Assuming nothing has made the input fail, you get a pass
    return "qualified"

if __name__ == "__main__":
    main()