#include "lists.h"
/**
 * insert_node - insert a number into a sorted singly linked list
 * @head: pointer to the head node
 * @number: element in the inserted node
 * Return: address of the new node or null if it fails
 */
listint_t *insert_node(listint_t **head, int number)
{
	listint_t *new_node;
	listint_t *current = *head;

	new_node = malloc(sizeof(listint_t));
	new_node->n = number;

	if (new_node == NULL)
		return (NULL);

	if (current == NULL || current->n >= new_node->n)
	{
		new_node->next = current;
		*head = new_node;
		return (new_node);
	}

	while (current->next && current->next->n < new_node->n)
	{
		current = current->next;
	}

	new_node->next = current->next;
	current->next = new_node;
	return (new_node);
}


