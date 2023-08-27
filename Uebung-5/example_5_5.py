# Bearbeitet durch Eric Böwer

import numpy as np


def generateAssetMatrix():
    m = n = 1000
    return np.random.uniform(0, 100000, size=(m, n))  # generate M with m = n = 1000


def generateBlock(transactions):
    block = {
        "Transactions": transactions.copy(),
        "HashKey": np.random.randint(0, int(1e10))
    }
    return block


def findMinMaxAssets(chain):
    minAsset = float("inf")
    maxAsset = float("-inf")

    for block in chain:
        for T in block["Transactions"]:
            A = T["Assets"]
            assetValueMax = np.max(A)
            assetValueMin = np.min(A)

            if assetValueMin < minAsset:
                minAsset = assetValueMin

            if assetValueMax > maxAsset:
                maxAsset = assetValueMax

    return minAsset, maxAsset


def simulate():
    blockChain = []
    numTransactions = 100
    assetsPerTransaction = 2

    for i in range(numTransactions):
        T = []
        for _ in range(assetsPerTransaction):
            A = generateAssetMatrix()
            T.append({"Assets": A})

        block = generateBlock(T)
        blockChain.append(block)

    minAsset, maxAsset = findMinMaxAssets(blockChain)

    print("Smallest Asset: ")
    print('{:20.20f}'.format(minAsset))
    print("\nLargest Asset: ")
    print('{:20.20f}'.format(maxAsset))


if __name__ == "__main__":
    simulate()
