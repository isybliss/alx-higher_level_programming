#include "lists.h"

listint_t *reverse_listint(listint_t **head);
int is_palindrome(listint_t **head);

/**
 * reverse_listint - Reverse a singly linked list
 * @head: pointer to the first node
 * Return: pointer to head of reversed list
 */

listint_t *reverse_listint(listint_t **head)
{
	listint_t *current = *head, *next, *prev = NULL;

	while (current)
	{
		next = current->next;
		current->next = prev;
		prev = current;
		current = next;
	}

	*head = prev;
	return (*head);
}

/**
 * is_palindrome - check if a singly linked list is palindrome
 * @head: pointer to first node
 * Return: 0 if not palindrome, 1 if palindrome
 */

int is_palindrome(listint_t **head)
{
	listint_t *tmp = *head, *rev, *mid;

	if (*head == NULL || (*head)->next == NULL)
		return (1);

	tmp = tmp->next->next;
	rev = reverse_listint(&tmp);
	mid = rev;

	tmp = *head;
	while (rev)
	{
		if (tmp->n != rev->n)
			return (0);
		tmp = tmp->next;
		rev = rev->next;
	}
	reverse_listint(&mid);

	return (1);
}
