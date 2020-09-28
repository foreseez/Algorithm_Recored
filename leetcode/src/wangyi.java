public class Main {
    public static int[] main(String[] args) {

        public int[] findmin(int[] array) {
            if (array == null) {
                return array;
            }
            int size = array.length;
            int[] res = new int[size];
            for (int i = 0; i < size - 1; i++) {
                for (int j = i + 1; j < size; j++) {
                    if (array[j] < array[i]) {
                        res[i] = j - i;
                    }
                    else {
                        res[i] = 0;
                    }


                }

            }
            return res;
        }

    }

}

def func(array):

