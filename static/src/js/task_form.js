$(document).ready(function () {
    var $projectSelect = $('#project_id');
    var $taskSelect = $('#task_id');

    // Загрузка списка задач при изменении выбранного проекта
    $projectSelect.on('change', function () {
        var projectId = $projectSelect.val();

        // Очистка текущего списка задач
        $taskSelect.empty();

        // Запрос на сервер для получения задач по выбранному проекту
        $.ajax({
            type: 'GET',
            url: '/timesheet/tasks',
            data: {
                'project_id': projectId
            },
            success: function (data) {
                // Добавление полученных задач в список
                data.forEach(function (task) {
                    $taskSelect.append('<option value="' + task.id + '">' + task.name + '</option>');
                });
            }
        });
    });

    // Trigger the change event to load tasks initially
    $projectSelect.trigger('change');
});
