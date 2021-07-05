import math
import numpy as np


def transform_weights(weights):
    return np.negative(np.log(weights))


def bellman_ford(source, weights):
    n = weights.shape[0]
    distance = [math.inf] * n
    predecessor = [-1] * n
    distance[source] = 0
    for _ in range(n - 1):
        for u in range(n):
            for v in range(n):
                if distance[u] + weights[u, v] < distance[v]:
                    distance[v] = distance[u] + weights[u, v]
                    predecessor[v] = u
    return distance, predecessor


def find_negative_cycles(weights):
    weights = transform_weights(weights)
    distance, predecessor = bellman_ford(0, weights)
    n = len(weights)
    negative_cycles = []
    for u in range(n):
        for v in range(n):
            if distance[u] + weights[u, v] < distance[v]:
                cycle = [v]
                while predecessor[v] not in cycle:
                    cycle.append(predecessor[v])
                    v = predecessor[v]
                cycle.append(predecessor[v])
                negative_cycles.append(cycle)
    return negative_cycles


def log_cycles(vertices, negative_cycles):
    for cycle in negative_cycles:
        print(' '.join([vertices[i] for i in reversed(cycle)]))


if __name__ == '__main__':
    currencies = np.load('forex_currencies.npy')
    exchange_rates = np.load('forex_exchange_rate_matrix.npy')
    cycles = find_negative_cycles(exchange_rates)
    log_cycles(currencies, cycles)
