<?php

$url = query;
$data = file_get_contents($url);
$characters = json_decode($data);

echo $characters[0]->name;

<table>
	<tbody>
		<tr>
			<th>Name</th>
			<th>Race</th>
		</tr>
		<?php foreach ($characters as $character) : ?>
        <tr>
            <td> <?php echo $character->user; ?> </td>
            <td> <?php echo $character->rcid; ?> </td>
        </tr>
		<?php endforeach; ?>
	</tbody>
</table>