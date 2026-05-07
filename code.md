int sumList(Node* head) {
    if (head == NULL)
    {
        return 0;
    }
    return head->data + sumList(head->next);
}