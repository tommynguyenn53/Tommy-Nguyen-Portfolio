public class Main {

    class Node<E> {
        private E element;
        private Node<E> next;

        public Node(E element) {
            this.element = element;
            this.next = next;
        }

        public E getElement() {
            return element;
        }

        public void setElement(E element) {
            this.element = element;
        }

        public Node<E> getNext() {
            return next;
        }

        public void setNext(Node<E> next) {
            this.next = next;
        }
    }

    class LinkedList<T> {
        private Node<T> head;
        private int size;

        public LinkedList() {
            head = null;
            size = 0;
        }

        public int size() {
            return size;
        }

        public T add(T element) {
            Node<T> newNode = new Node<>(element);
            if (head == null) {
                head = newNode;
            } else {
                Node<T> current = head;
                while (current.getNext() != null) {
                    current = current.getNext();
                }
                current.setNext(newNode);
            }
            size++;
            return element;
        }

        public T set(int index, T element) {
            if (index < 0 || index >= size) {
                throw new IndexOutOfBoundsException("Index out of bounds");
            }

            Node<T> current = head;
            for (int i = 0; i < index; i++) {
                current = current.getNext();
            }

            T oldValue = current.getElement();
            current.setElement(element);
            return oldValue;
        }

        public T get(int index) {
            if (index < 0 || index >= size) {
                throw new IndexOutOfBoundsException("Index out of bounds");
            }

            Node<T> current = head;
            for (int i = 0; i < index; i++) {
                current = current.getNext();
            }

            return current.getElement();
        }

        public T remove(int index) {
            if (index < 0 || index >= size) {
                throw new IndexOutOfBoundsException("Index out of bounds");
            }

            T removedElement;

            if (index == 0) {
                removedElement = head.getElement();
                head = head.getNext();
            } else {
                Node<T> current = head;
                for (int i = 0; i < index - 1; i++) {
                    current = current.getNext();
                }

                Node<T> nodeToRemove = current.getNext();
                removedElement = nodeToRemove.getElement();
                current.setNext(nodeToRemove.getNext());
            }
            size--;
            return removedElement;
        }
    }
}


