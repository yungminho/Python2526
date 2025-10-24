# Podać sposób wyświetlania stringu word tak,
# aby jego znaki były rozdzielone znakiem podkreślenia.

def underscore(word):
    return '_'.join(word)


def main():
    word = "Lorem ipsum dolor sit amet, consectetur adipiscing elit."
    expected = "L_o_r_e_m_ _i_p_s_u_m_ _d_o_l_o_r_ _s_i_t_ _a_m_e_t_,_ _c_o_n_s_e_c_t_e_t_u_r_ _a_d_i_p_i_s_c_i_n_g_ _e_l_i_t_."

    assert underscore(word) == expected

if __name__ == '__main__':
    main()