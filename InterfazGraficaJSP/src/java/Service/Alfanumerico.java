/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
package Service;

import java.util.Random;

/**
 *
 * @author Flinttloco
 */
public class Alfanumerico {

    public String Codigo() {
        String ret = "";

        Random rnd = new Random();
        String abecedario = "ABCDEFGHIJKLMOPQRSTUVWXYZ";
        String cadena = "";
        int m = 0, n = 0, pos = 0, num, pos1 = 0;
        while (m < 1) {
            while (n <= 4) {
                pos = (int) (rnd.nextDouble() * abecedario.length() - 1 + 0);
                num = (int) (rnd.nextDouble() * 99 + 10);
                cadena = cadena + abecedario.charAt(pos) + num;
                n++;

            }

            ret = cadena.substring(0, 15);
            m++;

        }
        return ret;
    }

}
