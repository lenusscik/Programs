def bishop(start_pos, end_pos, num_moves):
    st_num = str(ord(start_pos[0]) - 96) + start_pos[1]
    end_num = str(ord(end_pos[0]) - 96) + end_pos[1]
    if (st_num == end_num) and num_moves >= 0:
        return True    
    if num_moves > 0:
        if (int(st_num[0]) + int(st_num[1])) % 2 == (int(end_num[0]) + int(end_num[1])) % 2:
            if num_moves >= 2:
                return True
            elif ((int(st_num[0]) - int(st_num[1])) == (int(end_num[0]) - int(end_num[1]))) or ((int(st_num[0]) + int(st_num[1])) == (int(end_num[0]) + int(end_num[1]))):
                return True
            else:
                return False
        else:
            return False
    else:
        return False
    

print(bishop('d3', 'c2', 0))
