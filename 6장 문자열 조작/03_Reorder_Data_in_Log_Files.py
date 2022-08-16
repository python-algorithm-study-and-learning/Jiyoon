class Solution:
    def reorderLogFiles(self, logs: List[str]) -> List[str]:
        letter_logs = list()
        digit_logs = list()
        
        for log in logs:
            if log.split()[1].isdigit():
                digit_logs.append(log)
            else:
                letter_logs.append(log)
                
        letter_logs.sort(key=lambda x : (x.split()[1:], x.split()[0]))
        
        return letter_logs + digit_logs
