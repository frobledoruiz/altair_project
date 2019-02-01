<script type="text/javascript">
    var fascia_year = {{ selected_date|date:"Y" }}
    var selected_month = {{ selected_date|date:"m" }} - 1;
    var selected_day = {{ selected_date|date:"d"}}
    var selected_date = new Date(selected_year, selected_month, selected_day);
    alert(selected_date);
</script>