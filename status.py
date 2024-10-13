from status import format_progress_bar

# Example usage
total_items = 100
for current in range(total_items + 1):
    print(format_progress_bar(current, total_items))
    # Simulate some work being done
