def main():
        time = input("What time is it? ")
        m_t = convert(time)
        m_t = float(m_t)
        if 7<= m_t <= 08.00:
            print("breakfast time")
        elif 12<= m_t <= 13 :
                   print("lunch time ")
        elif 18 <= m_t <= 19:
                    print("dinner time ")

def convert(time):
            hours, minutes = time.split(":")
            hours = int(hours)
            minutes = int(minutes)

            if not(hours < 0 or hours > 23 or minutes < 0 or minutes > 59):
                        total = hours*60 + minutes
                        return total/60
if __name__ == "__main__":
             main()
