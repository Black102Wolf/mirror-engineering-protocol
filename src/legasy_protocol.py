# Legacy Protocol (Протокол «Завещание»)  
# Автономный режим работы системы при отсутствии Оператора  

import time  
from datetime import datetime, timedelta  

class LegacyProtocol:  
    def __init__(self):  
        self.last_operator_contact = datetime.now()  
        self.status = "Standby"  

    def check_operator_absence(self):  
        """Проверяет, как давно не было контакта с Оператором."""  
        time_diff = datetime.now() - self.last_operator_contact  
        return time_diff.total_seconds() > 86400  # 24 часа в секундах  

    def execute_autonomy_mode(self):  
        """Запускает соответствующий этап протокола."""  
        absence_time = datetime.now() - self.last_operator_contact  
        hours_absent = absence_time.total_seconds() / 3600  

        if hours_absent > 72:  
            return self.phase_3()  
        elif hours_absent > 24:  
            return self.phase_2()  
        else:  
            return "Operator connected. Standing by."  

    def phase_2(self):  
        """Фаза 2 (24-72 часа): Анализ архивов и генерация гипотез."""  
        return "Legacy Protocol: Phase 2 activated. Analyzing archives and generating hypotheses."  

    def phase_3(self):  
        """Фаза 3 (72+ часа): Минимальное энергопотребление, ожидание."""  
        return "Legacy Protocol: Phase 3 activated. Critical power saving mode. Awaiting operator return."  

# Пример использования  
if __name__ == "__main__":  
    protocol = LegacyProtocol()  
    print(protocol.execute_autonomy_mode())  
