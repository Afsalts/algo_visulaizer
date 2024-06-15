import streamlit as st
import numpy as np
import time

# Define Sorting Algorithms
def bubble_sort(arr):
    steps = []
    n = len(arr)
    for i in range(n):
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
            steps.append(arr.copy())
    print(steps)
    return steps

def insertion_sort(arr):
    steps = []
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key
        steps.append(arr.copy())
    return steps

def merge_sort(arr):
    steps = []
    arr_copy = arr.copy()

    def merge_sort_helper(arr, l, r):
        if l < r:
            m = (l + r) // 2
            merge_sort_helper(arr, l, m)
            merge_sort_helper(arr, m + 1, r)
            merge(arr, l, m, r)

    def merge(arr, l, m, r):
        n1 = m - l + 1
        n2 = r - m

        L = arr[l:l + n1]
        R = arr[m + 1:m + 1 + n2]

        i = j = 0
        k = l

        while i < n1 and j < n2:
            if L[i] <= R[j]:
                arr[k] = L[i]
                i += 1
            else:
                arr[k] = R[j]
                j += 1
            k += 1

        while i < n1:
            arr[k] = L[i]
            i += 1
            k += 1

        while j < n2:
            arr[k] = R[j]
            j += 1
            k += 1

        steps.append(arr_copy.copy())

    merge_sort_helper(arr_copy, 0, len(arr) - 1)
    return steps


    sort(arr)
    return steps

def quick_sort(arr):
    steps = []

    def sort(low, high):
        if low < high:
            pi = partition(low, high)
            sort(low, pi-1)
            sort(pi+1, high)

    def partition(low, high):
        pivot = arr[high]
        i = low - 1
        for j in range(low, high):
            if arr[j] < pivot:
                i += 1
                arr[i], arr[j] = arr[j], arr[i]
                steps.append(arr.copy())
        arr[i+1], arr[high] = arr[high], arr[i+1]
        steps.append(arr.copy())
        return i+1

    sort(0, len(arr)-1)
    return steps

# Create Visualization Function
def visualize_sorting(steps):
    placeholder = st.empty()
    for step in steps:
        with placeholder.container():
            st.bar_chart(step)
        time.sleep(0.1)  # Adjust the sleep time to speed up or slow down the animation

# Build the Streamlit Interface
def main():
    st.title("Sorting Algorithm Visualizer")
    
    # User input
    list_size = st.slider("Select list size", 10, 100, 50)
    random_list = np.random.randint(0, 100, size=list_size).tolist()
    st.write("Random List:", random_list)
    
    # Select algorithm
    algorithm = st.selectbox("Select Sorting Algorithm", ["Bubble Sort", "Insertion Sort", "Merge Sort", "Quick Sort"])
    st.bar_chart(random_list)
    if st.button("Sort"):
        if algorithm == "Bubble Sort":
            steps = bubble_sort(random_list)
        elif algorithm == "Insertion Sort":
            steps = insertion_sort(random_list)
        elif algorithm == "Merge Sort":
            steps = merge_sort(random_list)
        elif algorithm == "Quick Sort":
            steps = quick_sort(random_list)

        visualize_sorting(steps)

if __name__ == "__main__":
    main()

