class Work:
    
    def write_notes(self, note):
        with open ('file.csv', 'a', encoding="utf-8") as data:
            data.write(note)
            
    
    def read_notes(self):
        with open ('file.csv', 'r', encoding="utf-8") as data:
            a = True
            while a == True:
                file_line = data.readline()
                print(file_line)
                if not file_line:
                    print("End Of File")
                    a = False

    def read_note(self, name):
        with open ('file.csv', 'r', encoding="utf-8") as data:
            a = True
            while a == True:
                file_line = data.readline()
                check_name = file_line.split()
                if check_name[0] == name:
                    print(file_line)
                    break
                if not file_line:
                    print("not found")
                    a = False 
    
    def del_note (self, name):
        with open ('file.csv', 'r', encoding="utf-8") as data:
            l = data.readlines()
            for i in range(len(l)):
                a = l[i].split()
                if a[0] == name:
                    pos = i
            if (pos >= 0) and (pos < len(l)):
                i = pos
                while i<len(l)-1:
                    l[i] = l[i+1]
                    i = i+1
                l = l[:-1]
        with open ('file.csv', 'w', encoding="utf-8") as data:
            for line in l:
                data.write(line)
                print(f"Заметка {name} успешно удалена")