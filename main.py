import time

# Simulate an in-memory cache using a dictionary.
# In a real-world scenario, this could be a more sophisticated cache library
# or an external service like Redis/Memcached.
cache = {}

def expensive_operation(key):
    """
    Simulates an expensive operation like a database query, API call, or complex computation.
    It introduces a 2-second delay to represent the cost.
    """
    print(f"Performing expensive operation for key: '{key}'...")
    time.sleep(2)  # Simulate delay for an expensive task
    result = f"Data for {key} (generated at {time.ctime()})"
    print(f"Finished expensive operation for key: '{key}'.")
    return result

def get_data_with_cache(key):
    """
    Retrieves data, prioritizing the cache. If data is not found in the cache,
    it performs the expensive operation and stores the result for future use.
    """
    # 1. Check if the data is already in the cache (Cache Hit)
    if key in cache:
        print(f"Cache hit for key: '{key}' - retrieving from cache.")
        return cache[key]  # Return cached data immediately
    
    # 2. If not in cache, perform the expensive operation (Cache Miss)
    print(f"Cache miss for key: '{key}' - performing expensive operation.")
    data = expensive_operation(key)
    
    # 3. Store the result in the cache for future requests
    cache[key] = data
    print(f"Stored result for key: '{key}' in cache.")
    return data

if __name__ == "__main__":
    print("--- First call for 'product_details_123' ---")
    start_time = time.time()
    data1 = get_data_with_cache("product_details_123")
    end_time = time.time()
    print(f"Result: {data1}")
    print(f"Time taken: {end_time - start_time:.2f} seconds\n")

    print("--- Second call for 'product_details_123' (should be fast due to caching) ---")
    start_time = time.time()
    data2 = get_data_with_cache("product_details_123")
    end_time = time.time()
    print(f"Result: {data2}")
    print(f"Time taken: {end_time - start_time:.2f} seconds\n")

    print("--- First call for 'user_profile_456' ---")
    start_time = time.time()
    data3 = get_data_with_cache("user_profile_456")
    end_time = time.time()
    print(f"Result: {data3}")
    print(f"Time taken: {end_time - start_time:.2f} seconds\n")

    print("--- Third call for 'product_details_123' (still fast) ---")
    start_time = time.time()
    data4 = get_data_with_cache("product_details_123")
    end_time = time.time()
    print(f"Result: {data4}")
    print(f"Time taken: {end_time - start_time:.2f} seconds\n")

    print("\nCache contents after operations:")
    for key, value in cache.items():
        print(f"  '{key}': {value}")
