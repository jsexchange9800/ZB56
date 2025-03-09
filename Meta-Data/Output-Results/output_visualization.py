import matplotlib.pyplot as plt
import json

def visualize_results(results_file):
    """Visualize the results stored in the JSON file"""
    with open(results_file, 'r') as file:
        results = json.load(file)
    # Example: Plotting the results
    plt.plot(results['x'], results['y'])
    plt.title('Model Results Visualization')
    plt.xlabel('X-axis')
    plt.ylabel('Y-axis')
    plt.show()
