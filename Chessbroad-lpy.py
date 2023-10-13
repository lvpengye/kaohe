from collections import defaultdict  
  
def count_positions(n, moves):  
    positions = defaultdict(int)  
  
    for i in range(n):  
        move = moves[i]  
        key = '*'.join(move[1:-1])  # Exclude边界字符'('和')'  
        positions[key] += 1  
  
    return dict(positions)  
  
# 主函数  
def main():  
    n = int(input().strip())  
    moves = []  
  
    for _ in range(n * 8):  
        move = input().strip()  
        moves.append(move)  
  
    result = count_positions(n, moves)  
  
    for k, v in result.items():  
        print(f"{k}: {v}")  
  
if __name__ == '__main__':  
    main()