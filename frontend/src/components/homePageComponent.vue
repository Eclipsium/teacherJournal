<template>
    <v-content>
        <v-container>
            <v-card>
                <v-card-title>
                    Список студентов
                    <v-spacer></v-spacer>
                    <v-text-field
                            v-model="search"
                            append-icon="mdi-magnify"
                            label="Поиск"
                            single-line
                            hide-details
                    ></v-text-field>
                </v-card-title>
                <v-data-table
                        :headers="headers"
                        :items="students"
                        :search="search"
                        hide-default-footer
                        disable-pagination
                >

                    <template v-slot:item.math="{item}">
                        <span :class="getColorForRate(item.math)">{{item.math}}</span>
                        <v-btn icon small color="warning" @click="editStudent(item, 'math')">
                            <v-icon x-small>
                                mdi-pencil
                            </v-icon>
                        </v-btn>
                    </template>

                    <template v-slot:item.physic="{item}">
                        <span :class="getColorForRate(item.physic)">{{item.physic}}</span>
                        <v-btn icon small color="warning" @click="editStudent(item, 'physic')">
                            <v-icon x-small>
                                mdi-pencil
                            </v-icon>
                        </v-btn>
                    </template>

                    <template v-slot:item.russian="{item}">
                        <span :class="getColorForRate(item.russian)">{{item.russian}}</span>
                        <v-btn icon small color="warning" @click="editStudent(item, 'russian')">
                            <v-icon x-small>
                                mdi-pencil
                            </v-icon>
                        </v-btn>
                    </template>

                    <template v-slot:item.english="{item}">
                        <span :class="getColorForRate(item.english)">{{item.english}}</span>
                        <v-btn icon small color="warning" @click="editStudent(item, 'english')">
                            <v-icon x-small>
                                mdi-pencil
                            </v-icon>
                        </v-btn>
                    </template>

                    <template v-slot:item.name=" { item } ">
                        <span class="text-capitalize">{{item.name}}</span>
                    </template>
                </v-data-table>
            </v-card>
        </v-container>
        <v-dialog
                v-model="editStudentDialog"
                width="500"
        >
            <v-card>
                <v-card-title
                        class="grey lighten-2"
                        primary-title
                >
                    Изменить оценку для {{this.editedStudent.name}}
                </v-card-title>

                <v-card-text class="mt-2">
                    <p class="subtitle-1 text-center">{{getFullDisciplineName(this.editedDiscipline)}}</p>
                    <v-form
                            v-model="valid"
                    >
                        <v-text-field
                                v-model="tempRate"
                                :rules="digitRules"
                                :hint="getFullDisciplineName(this.editedDiscipline)"
                        ></v-text-field>
                    </v-form>

                </v-card-text>

                <v-divider></v-divider>

                <v-card-actions>
                    <v-btn
                            color="warning"
                            text
                            @click="editStudentDialog = false"
                    >
                        Отменить
                    </v-btn>
                    <v-spacer></v-spacer>
                    <v-btn
                            color="success"
                            :disabled="!this.valid"
                            text
                            @click="submitRate()"
                    >
                        Сохранить
                    </v-btn>
                </v-card-actions>
            </v-card>
        </v-dialog>
    </v-content>
</template>

<script>
    export default {
        name: 'HelloWorld',
        computed: {},
        mounted() {
            this.axios
                .get('http://localhost:8000/api/v1/rates/')
                .then((response) => {
                    this.students = response.data.results
                })
        },
        methods: {
            getColorForRate(rate) {
                if (rate >= 4) return 'success--text font-weight-medium';
                if (rate === 3) return 'warning--text font-weight-medium';
                return 'error--text font-weight-medium'
            },
            submitRate() {
                let payload = this.editedStudent;
                payload[this.editedDiscipline] = parseInt(this.tempRate);

                for (let index in this.students) {
                    if (payload.id === this.students[index].id) {
                        this.axios.put('http://localhost:8000/api/v1/rates/' + this.students[index].id + '/', payload)
                            .then(this.students[index] = payload)
                    }
                }
                this.editStudentDialog = false
            },
            getFullDisciplineName(shortDiscipline) {
                for (let index in this.headers) {
                    if (this.headers[index].value === shortDiscipline) {
                        return this.headers[index].text
                    }
                }
            },
            editStudent(student, discipline) {
                this.editedStudent = student;
                this.editedDiscipline = discipline;
                this.tempRate = student[discipline];
                this.editStudentDialog = true;
            },
        },
        data() {
            return {
                valid: true,
                tempRate: 0,
                loading: false,
                editStudentDialog: false,
                editedStudent: '',
                editedDiscipline: '',
                digitRules: [
                    v => (v && v >= 1 && v <= 5) || 'Оценка должна быть от 1 до 5',
                ],
                nameRules: [
                    v => !!v || 'Поле обязательно',
                    v => (v && v.length >= 3) || 'Поле должно содержать минимум 3 символа',
                ],
                newStudentDialog: false,
                newDisciplineDialog: false,
                search: '',
                headers: [
                    {text: '#', value: 'id'},
                    {
                        text: 'Имя студента',
                        align: 'start',
                        sortable: true,
                        value: 'name',
                    },
                    {text: 'Математика', value: 'math'},
                    {text: 'Физика', value: 'physic'},
                    {text: 'Русский язык', value: 'russian'},
                    {text: 'Английский язык', value: 'english'},
                ],
                students: []
            }
        }
        ,
    }
</script>
