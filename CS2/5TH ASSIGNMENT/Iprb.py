k = int(input('Insert the number of dominant homozygotes: '))
m = int(input('Insert the number of heterozygotes: '))
n = int(input('Insert the number of recessive homozygotes: '))

total = k + m + n

k_prob = k / total
m_prob = m / total
n_prob = n / total

mk_prob = (m_prob * (k / (total - 1)))
mm_prob = (m_prob * ((m - 1) / (total -1)))
mm_prob *= (3 / 4)
mn_prob = (m_prob * (n/ (total - 1)))
mn_prob *= (1/2)

nk_prob = (n_prob * (k / (total - 1)))
nm_prob = (n_prob * (m / (total - 1)))
nm_prob *= (1/2)

tot_prob = k_prob + mk_prob + mm_prob + mn_prob + nk_prob + nm_prob

print(tot_prob)