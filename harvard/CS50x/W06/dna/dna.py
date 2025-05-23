import csv
import sys


def main():
    # Check for command-line usage
    if len(sys.argv) != 3:
        print("Usage: python dna.py data.csv sequence.txt")
        return

    # Read database file into a variable
    database_file = sys.argv[1]
    dna_sequence_file = sys.argv[2]

    with open(database_file, 'r') as file:
        reader = csv.DictReader(file)
        profiles = list(reader)
        str_keys = reader.fieldnames[1:]

    # Read DNA sequence file into a variable
    with open(dna_sequence_file, 'r') as file:
        dna_sequence = file.read()

    # Find longest match of each STR in DNA sequence
    str_counts = {}
    for str_key in str_keys:
        count = longest_match(dna_sequence, str_key)
        str_counts[str_key] = str(count)

    # Check database for matching profiles
    match_found = False
    for profile in profiles:
        profile_counts = {key: profile[key] for key in str_keys}
        if profile_counts == str_counts:
            print(profile['name'])
            match_found = True
            break

    if not match_found:
        print("No match")

    return


def longest_match(sequence, subsequence):
    """Returns length of longest run of subsequence in sequence."""

    # Initialize variables
    longest_run = 0
    subsequence_length = len(subsequence)
    sequence_length = len(sequence)

    # Check each character in sequence for most consecutive runs of subsequence
    for i in range(sequence_length):

        # Initialize count of consecutive runs
        count = 0

        # Check for a subsequence match in a substring within sequence
        # If a match, move substring to next potential match in sequence
        # Continue moving substring and checking for matches until out of consecutive matches
        while True:

            # Adjust substring start and end
            start = i + count * subsequence_length
            end = start + subsequence_length

            # If there is a match in the substring
            if sequence[start:end] == subsequence:
                count += 1

            # If there is no match in the substring
            else:
                break

        # Update most consecutive matches found
        longest_run = max(longest_run, count)

    # After checking for runs at each character in seqeuence, return longest run found
    return longest_run


if __name__ == "__main__":
    main()
