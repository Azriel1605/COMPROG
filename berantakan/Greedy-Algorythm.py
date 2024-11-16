def greedy_coin_change(amount, coins):
    # Mengurutkan koin dalam urutan menurun
    coins.sort(reverse=True)
    
    # List untuk menyimpan hasil
    result = []
    
    # Iterasi melalui setiap koin
    for coin in coins:
        # Menentukan berapa banyak koin saat ini dapat digunakan
        count = amount // coin
        if count > 0:
            result.append((coin, count))
        # Mengurangi jumlah uang yang harus dikembalikan
        amount = amount % coin
    
    # Jika masih ada sisa uang yang belum bisa dikembalikan
    if amount != 0:
        print(f"Kembalian tidak dapat diberikan secara tepat dengan koin yang tersedia.")
    else:
        return result

# Contoh penggunaan
coins = [1, 2, 5, 10, 25]
amount = 70

result = greedy_coin_change(amount, coins)

if result:
    print(f"Kembalian untuk {amount} adalah:")
    for coin, count in result:
        print(f"{count} koin(s) dari {coin}")
