import statistics 

def calculate_stats(data):
    """
    Calculates the Mean, Median, Mode, and Range of a list.
    """
    data.sort()
    
    mean_val = sum(data) / len(data)
    median_val = statistics.median(data)
    
    # Handle the Mode: If there's a tie or no mode, we take the max value
    try:
        mode_val = statistics.mode(data)
    except statistics.StatisticsError:
        mode_val = max(data)
        
    range_val = max(data) - min(data)
    
    return [mean_val, median_val, mode_val, range_val]

def run_convergence(initial_set, max_iterations=20):
    """
    Runs the feedback loop until all four stats match or max_iterations is reached.
    """
    current_set = initial_set
    print(f"Starting Set: {current_set}")
    print("-" * 50)

    for i in range(1, max_iterations + 1):
        # Generate the new stats
        new_stats = calculate_stats(current_set)
        
        # Format for clean printing
        formatted_stats = [round(x, 4) for x in new_stats]
        print(f"Iteration {i}: {formatted_stats}")

        # Check if they all match (Agreement)
        # We use a small epsilon for float comparison
        if all(abs(x - new_stats[0]) < 1e-9 for x in new_stats):
            print("-" * 50)
            print(f"Agreement reached in {i} iterations: {new_stats[0]}")
            return

        # The output of the stats becomes the input for the next round
        current_set = new_stats

    print("-" * 50)
    print("Reached max iterations without perfect agreement.")

# Example Usage
if __name__ == "__main__":
    # Your example starting numbers
    start = [2, 2, 2]
    run_convergence(start)
