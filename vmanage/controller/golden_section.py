import time
import math

alpha = 2

#goodput = 20
#G = -2*((N-6)^2) + 72

golden_ratio = (3 - math.sqrt(5))/2
print "golden_ratio = ",golden_ratio

def G(N):
        return -2*((N - 6)**2) + 72

def search_bracket():
        #global N, G_N, G_N_1, G_N_2, iter, alpha
        global alpha
        iter = 1
        N = 1; N_1 = 1; N_2 = 1

        G_N = 0; G_N_1 = 0; G_N_2 = 0
        print "iter, N, G_N, G_N_1, G_N_2, (G_N >= G_N_1)"

        #while int(G_N) >= int(G_N_1):
                #G_N = 20 * N
        while True:
                G_N = -2*((N-6)**2) + 72
                G_N = G(N)
#               G_N = -2*(N-6)*(N-6) + 72
                print iter, N, G_N, G_N_1, G_N_2, (G_N >= G_N_1)
                if G_N < G_N_1:
                        break

                G_N_1 = G_N
                N_2 = N_1
                N_1 = N
                N *= alpha
                iter += 1
                #time.sleep(1)
                #goodput = goodput * N
        return (N_2, N_1, N)
        #return (2,4,8)

#def golden_section(bracket):
#       print bracket
def golden_section_search((l, m, r)):
        global golden_ratio
        #print "l = ",l," m = ",m," r = ",r
        while True:
                N = m + (r - m)*golden_ratio
                if (r - m) < (m - l):
                        N = l + (m - l)*golden_ratio
                N = round(N)

                time.sleep(1)

                G_N = G(N)
                G_m = G(m)
                print N, G_N, G_m
                if G_N > G_m:
                        if N > m:
                                golden_section_search((m, N, r))
                        else:
                                golden_section_search((l, N, m))
                else:
                        if N > m:
                                golden_section_search((l, m, N))
                        else:
                                golden_section_search((N, m, r))


bracket = search_bracket()
golden_section_search(bracket)

