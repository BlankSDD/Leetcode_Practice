# 1093. 大样本统计

class Solution:
    def sampleStats(self, count):
        m1 = -1
        m2 = -1
        m3 = -1
        m4 = -1
        m5 = -1

        s3_num = sum(count)
        s3_sum = 0
        s3 = []

        f4 = False
        if (s3_num & 1):
            f4 = True
        f4_num = s3_num//2 + 1
        f4_divide = False
        f4_ok = False

        t5_max = 0
        
        if f4:
            for i,t in enumerate(count):
                if t != 0:
                    s3_sum += i*t
                    s3.append(i)

                    if not f4_ok:
                        f4_num -= t
                        if f4_num <= 0:
                            m4 = i
                            f4_ok = True
                    
                    if t > t5_max:
                        t5_max = t
                        m5 = i
        else:
            for i,t in enumerate(count):
                if t != 0:
                    s3_sum += i*t
                    s3.append(i)

                    if not f4_ok:
                        f4_num -= t
                        if f4_num == 1:
                            m4 = i
                            f4_divide = True
                        elif f4_num < 1:
                            if f4_divide:
                                m4 = (m4+i) / 2
                            else:
                                m4 = i
                            f4_ok = True
                    
                    if t > t5_max:
                        t5_max = t
                        m5 = i
        
        m1 = s3[0]
        m2 = s3[-1]
        m3 = s3_sum / s3_num

        return [m1, m2, m3, m4, m5]
        
